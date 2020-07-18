from django.db import IntegrityError
from django.contrib.auth.hashers import check_password
from django.conf import settings

from rest_framework.exceptions import MethodNotAllowed
from rest_framework.generics import  ListCreateAPIView, CreateAPIView
from rest_framework import permissions, status
from rest_framework.response import Response

import jwt

from .models import User
from .serializers import UserSerializer
from .permissions import UserPermission


class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.filter()
    serializer_class = UserSerializer


    def get_permissions(self):
        if self.request.method == 'POST':
            return (permissions.AllowAny(),)
        elif self.request.method == 'GET':
            return (UserPermission('can_get_users'), )
        raise MethodNotAllowed(method=self.request.method)
    


    def create(self, request, *args, **kwargs):
        if 'superuser' in request.data.get('groups'):
            return Response({'message': 'can not assign user in superuser group'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.create_user(
                first_name=self.request.data['first_name'],
                last_name=self.request.data['last_name'],
                gender=self.request.data.get('gender', 'male'),
                email=self.request.data['email'],
                password=self.request.data['password'],
                groups=self.request.data.get('groups'),
                
            )
            serializer = self.get_serializer(user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        except IntegrityError as e:
            return Response(data={
                'message':f'can not create user . reason:{e}'
            }, status=status.HTTP_409_CONFLICT)  



class UserLogin(CreateAPIView):
    serializer_class = UserSerializer
    permission_class = (permissions.AllowAny, )
    query_set = User.objects.filter()


    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = User.objects.get(email__exact=email)
            verify_password = check_password(password=password, encoded=user.password)

            if not user.is_active:
                return Response({'message': 'user is not an active user'}, status=status.HTTP_406_NOT_ACCEPTABLE)

            if not verify_password:
                return Response({'message': 'password is incorrect'}, status=status.HTTP_401_UNAUTHORIZED)

            token = jwt.encode(payload=self.get_serializer(user).data, key=settings.SECRET_KEY, algorithm='HS256').decode('utf-8')    
            return Response({'token':token}, status=status.HTTP_201_CREATED)

        except User.DoesNotExist:
            return Response({'message': 'user does not exist'}, status=status.HTTP_404_NOT_FOUND)       



class ChangePassword(CreateAPIView):
    serializer_class = UserSerializer
    query_set = User.objects.filter()

    def get_permissions(self):
        if self.request.method == 'POST':
            return (UserPermission('can_change_password'), )
        raise MethodNotAllowed(method=self.request.method)

    def create(self, request, *args, **kwargs):
        user = self.request.user
        verify_password = check_password(password=request.data.get('old_password'), encoded=str(user.password), )
        
        if not verify_password:
            return Response({'message': 'password does not match with old password'}, status=status.HTTP_400_BAD_REQUEST)

        if request.data.get('old_password') == request.data.get('new_password'):
            return Response({'message':'new password and old pasword will not be same'}, status=status.HTTP_400_BAD_REQUEST)

        if request.data.get('new_password') != request.data.get('confirm_password'):
            return Response({'message':'new password and old password does not match'}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(request.data.get('new_password'))
        user.save()
        serializer = self.get_serializer(user)
        resp = {
            'data':serializer.data,
            'info': f'{user.email} has change the password',

        }
        return Response(data=resp, status=status.HTTP_201_CREATED)


       








         
            
               
            






