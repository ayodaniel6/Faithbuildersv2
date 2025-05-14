from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('posts/<slug:slug>/', views.post_detail, name='post_detail'),
    path('posts/<slug:slug>/add-comment/', views.add_comment, name='add_comment'),
    path('posts/<int:pk>/like/', views.like_post, name='like_post'),
    path('posts/<int:pk>/bookmark/', views.toggle_bookmark, name='toggle_bookmark'),
    path('blog/search/', views.SearchView.as_view(), name='search')
]
