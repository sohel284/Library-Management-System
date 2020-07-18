from django.urls import path

from .views import AuthorListCreateAPIView, BookListCreateAPIView



urlpatterns = [
    path('authors/', AuthorListCreateAPIView.as_view(), name='author -create-api'),
    path('books/', BookListCreateAPIView.as_view(), name='book-create-api'),
]