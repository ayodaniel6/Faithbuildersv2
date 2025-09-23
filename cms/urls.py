from django.urls import path
from . import views

app_name = 'cms'

urlpatterns = [
    path('dashboard/', views.cms_dashboard, name='admin_dashboard'),
    path('posts/', views.post_list, name='admin_post_list'),
    path('posts/create/', views.post_create, name='admin_post_create'),
    path('posts/<int:pk>/edit/', views.post_edit, name='admin_post_edit'),
    path('posts/<int:pk>/delete/', views.post_delete, name='admin_post_delete'),
    path('comments/', views.comment_list, name='admin_comment_list'),
    path('comments/<int:comment_id>/delete/', views.comment_delete, name='admin_comment_delete'),
    path('requests/', views.manage_requests, name='manage_requests'),
    path('api/', views.restfulAPIView, name='restfulAPI'),
]
