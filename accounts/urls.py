from django.urls import path
from .views import LogoutView, AuthView, DashboardView, ChangePasswordView
from . import views

app_name = 'accounts'

urlpatterns = [
    path('auth/', AuthView.as_view(), name='auth'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('auth/change-password/', ChangePasswordView.as_view(), name='change_password'),
]
