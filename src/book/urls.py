from django.urls import path

from .views import AuthorListCreateAPIView, BookListCreateAPIView
from .views import CopyOfBookListCreateAPIView



urlpatterns = [
    path('authors/', AuthorListCreateAPIView.as_view(), name='author -create-api'),
    path('books/', BookListCreateAPIView.as_view(), name='book-create-api'),
    path('copy_of_books/', CopyOfBookListCreateAPIView.as_view(), name='copy-book-create-api'),
]
