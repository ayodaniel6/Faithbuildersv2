from django.db import models
from django.utils import timezone

class CounsellorRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Request by {self.name} on {self.created_at.strftime('%Y-%m-%d')}"
