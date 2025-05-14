from django.urls import path
from .views_api import CounsellorRequestListCreateAPIView, CounsellorRequestRetrieveAPIView

urlpatterns = [
    path('counsellor-requests/', CounsellorRequestListCreateAPIView.as_view(), name='counsellor-request-list-create'),
    path('counsellor-requests/<int:pk>/', CounsellorRequestRetrieveAPIView.as_view(), name='counsellor-request-detail'),
]
