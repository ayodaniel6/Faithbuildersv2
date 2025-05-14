from django.urls import path
from .views_api import UserListAPIView, ProfileDetailAPIView

urlpatterns = [
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('profile/', ProfileDetailAPIView.as_view(), name='profile-detail'),
]
