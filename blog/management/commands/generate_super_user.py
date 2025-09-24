from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from decouple import config

User = get_user_model()

class Command(BaseCommand):
    help = "Ensure a superuser exists (uses environment variables)"

    def handle(self, *args, **kwargs):
        admin_username = config("DJANGO_SUPERUSER_USERNAME", default="admin")
        admin_email = config("DJANGO_SUPERUSER_EMAIL", default="admin@example.com")
        admin_password = config("DJANGO_SUPERUSER_PASSWORD", default="admin123")

        if not User.objects.filter(username=admin_username).exists():
            User.objects.create_superuser(
                username=admin_username,
                email=admin_email,
                password=admin_password,
            )
            self.stdout.write(self.style.SUCCESS(
                f"✅ Superuser '{admin_username}' created."
            ))
        else:
            self.stdout.write(self.style.WARNING(
                f"⚠️ Superuser '{admin_username}' already exists."
            ))
