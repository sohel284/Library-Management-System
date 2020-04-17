from django.urls import path

from books.views import AuthorListCreateAPIView, AuthorRetrieveDestroyAPIView

path('', AuthorListCreateAPIView.as_view(), name='author create', ),
path('<int:id>/', AuthorRetrieveDestroyAPIView.as_view(), name='author update', ),
