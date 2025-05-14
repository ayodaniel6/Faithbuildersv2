from rest_framework import viewsets, permissions
from blog.models import Post, Comment
from .serializers import PostCMSAdminSerializer, CommentModerationSerializer

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class PostAdminViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostCMSAdminSerializer
    permission_classes = [IsAdminOrReadOnly]

class CommentModerationViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentModerationSerializer
    permission_classes = [IsAdminOrReadOnly]
