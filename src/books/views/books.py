from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework import permissions

from books.models import Book
from books.serializers import BookSerializer
from books.serializers import AuthorSerializer


class BookListCreateAPIView(ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = BookSerializer
    queryset = Book.objects.filter()
    lookup_field = 'id'



