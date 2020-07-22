from django.core.exceptions import ObjectDoesNotExist

from rest_framework.generics import ListCreateAPIView
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import MethodNotAllowed

import json

from user.models import User
from book.models import CopyOfBook
from borrow.models import Borrow
from user.permissions import UserPermission

from borrow.serializers import BorrowSerializer


class BorrowListCreateAPIView(ListCreateAPIView):
    serializer_class = BorrowSerializer
    queryset = Borrow.objects.all()


    def get_permission(self):
        if self.request.method == 'POST':
            return UserPermission(('can_borrow_books'), )
        elif self.request.method == 'GET':
            return (permissions.AllowAny(),)
        raise MethodNotAllowed(method=self.request.method, )

    def create(self, request, *args, **kwargs):



        user = self.request.user
        payload = json.loads(request.body)

         
         

        try:
            
            borrow_book = CopyOfBook.objects.get(id=payload['borrow_book'])
            
            borrow = Borrow.objects.create(
                borrow_book=borrow_book,
                user=user,
                issue_date=payload['issue_date'],
                return_date=payload['return_date'],
            )
           
           
            serializer = self.get_serializer(borrow)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED, )
        except ObjectDoesNotExist as e:
            return Response({'error':'can not borrow book'}, status=status.HTTP_404_NOT_FOUND, )

              
            
