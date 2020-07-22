from django.conf import Settings
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.generics import ListCreateAPIView
from rest_framework import permissions, status
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response

import json

from book.models import Author, Book, CopyOfBook
from book.serializers import AuthorSerializer, BookSerializer, CopyOfBookSerializer
from user.permissions import UserPermission
from user.models import User



class AuthorListCreateAPIView(ListCreateAPIView):
  
    serializer_class = AuthorSerializer
    queryset = Author.objects.filter()


    def get_permission(self):
        if self.request.method == 'POST':
            return (UserPermission('can_add_authors'), )
        elif self.request.method == 'GET':
            return (permissions.AllowAny(), ) 
        raise MethodNotAllowed(method=self.request.method)
    

    def create(self, request, *args, **kwargs):
        user = self.request.user
       

        try:
            author = Author.objects.create(
                first_name=self.request.data['first_name'],
                last_name =self.request.data['last_name'],
                date_of_birth=self.request.data['date_of_birth'],
                date_of_died=self.request.data['date_of_died'],
                added_by=user
            )
            serializer = self.get_serializer(author)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        except ObjectDoesNotExist as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

class BookListCreateAPIView(ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.filter()

    def get_permission(self):
        if self.request.method == 'POST':
            return (UserPermission('can_add_books'), )
        elif self.request.method == 'GET':
            return (permissions.AllowAny(), )
        raise MethodNotAllowed(method=self.request.method)

    def create(self, request, *args, **kwargs):
      
        user = self.request.user
        payload = json.loads(request.body)
        try:
           
            author = Author.objects.get(id=payload['author'])    
            book = Book.objects.create(
                isbn=payload['isbn'],
                book_name=payload['book_name'],
                author=author,
                edition=payload['edition'],
                summary=payload['summary'],
                genre=payload['genre'],
                language=payload['language'],
                status=payload['status'],
                price =payload['price'],
                added_by= user,
            )
            
            
            
            serializer = self.get_serializer(book)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND) 




class CopyOfBookListCreateAPIView(ListCreateAPIView):
    serializer_class = CopyOfBookSerializer
    queryset = CopyOfBook.objects.filter()

    def get_permission(self):
        if self.request.method == 'POST':
            return (UserPermission('can_add_copy_of_book'), )
        elif self.request.method == 'GET':
            return (permissions.AllowAny(), )
        return MethodNotAllowed(method=self.request.method)

    def create(self, request, *args, **kwargs):
        payload = json.loads(request.body)

        try:
            book = Book.objects.get(isbn=payload['book'])

            copy_book = CopyOfBook.objects.create(
                copy_of_book_code=payload['copy_of_book_code'],
                book=book,
                quantity=payload['quantity'],
            )  
            serializer = self.get_serializer(copy_book)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)              


        
        
        
    
                           









