from rest_framework import generics, permissions
from bot.models import CounsellorRequest
from .serializers import CounsellorRequestSerializer

class CounsellorRequestListCreateAPIView(generics.ListCreateAPIView):
    queryset = CounsellorRequest.objects.all()
    serializer_class = CounsellorRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

class CounsellorRequestRetrieveAPIView(generics.RetrieveAPIView):
    queryset = CounsellorRequest.objects.all()
    serializer_class = CounsellorRequestSerializer
    permission_classes = [permissions.IsAuthenticated]
