from django.core.management.base import BaseCommand

from authentication.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username="root"):
            print("Creating admin account...")
            User.objects.create_superuser(
                email="admin@example.com",
                username="root",
                password="cryptonsquad1337",
                is_active=True,
                is_account_activated=True,
            )
        else:
            print("Admin already initialized")
