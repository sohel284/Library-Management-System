from django.urls import path

from books.views import BookListCreateAPIView, BookRetrieveDestroyAPIView


urlpatterns = [
    path('', BookListCreateAPIView.as_view(), name='Book create', ),
    path('<int:id>/', BookRetrieveDestroyAPIView.as_view(), name='book update', ),


]
