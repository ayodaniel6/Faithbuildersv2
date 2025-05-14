from rest_framework import serializers
from blog.models import Post, Comment

class PostCMSAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentModerationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
