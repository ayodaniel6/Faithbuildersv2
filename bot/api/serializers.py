from rest_framework import serializers
from bot.models import CounsellorRequest

class CounsellorRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CounsellorRequest
        fields = ['id', 'name', 'email', 'message', 'created_at']
        read_only_fields = ['id', 'created_at']
