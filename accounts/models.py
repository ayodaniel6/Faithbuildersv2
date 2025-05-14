from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def user_avatar_path(instance, filename):
    return f'accounts/images/avatars/user_{instance.user.id}/{filename}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, max_length=255)
    avatar = models.ImageField(upload_to=user_avatar_path, blank=True, null=True)

    def __str__(self):
        return self.user.username
