from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'bot'

urlpatterns = [
    path('request/', views.request_counsellor, name='request'),
    path('reply/', views.bot_reply, name='bot_reply'),
    path('thank-you/', TemplateView.as_view(template_name='bot/thank_you.html'), name='thank_you'),
]
