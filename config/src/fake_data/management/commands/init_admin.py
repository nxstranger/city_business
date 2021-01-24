from django.core.management.base import BaseCommand
from src.user.models import Human
import os


class Command(BaseCommand):
    """
    """
    def handle(self, *args, **options):
        """
        """
        try:
            self.create_admin()
        except Exception as ex:
            print(ex)
            self.stdout.write('Error while try create admin profile')

    def create_admin(self):
        if Human.objects.count() == 0:
            user = Human(
                username="admin",
                is_active=True,
                is_staff=True,
                is_superuser=True,
                )
            user.set_password(os.environ.get('DJANGO_SUPERUSER_PASSWORD'))
            user.save()
            self.stdout.write('Admin created')

