from django.urls import path
from .views import BorrowListCreateAPIView

urlpatterns = [
    path('', BorrowListCreateAPIView.as_view(), name='borrow-create-api', )
]