from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework import permissions

from books.models import Author
from books.serializers import AuthorSerializer


class AuthorListCreateAPIView(ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class AuthorRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = AuthorSerializer
    queryset = Author.objects.filter()
    lookup_field = 'id'
