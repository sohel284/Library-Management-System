from django.urls import path
from .views import UserListCreateAPIView, UserLogin, ChangePassword


urlpatterns = [
    path('', UserListCreateAPIView.as_view(), name='user-list-create -api'),
    path('login/', UserLogin.as_view(), name='user-login'),
    path('change-password/', ChangePassword.as_view(), name='user-change-pass'),

]

