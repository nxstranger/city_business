from django.core.management.base import BaseCommand
from src.user.models import Human


class Command(BaseCommand):
    """
    """
    def handle(self, *args, **options):
        """
        """
        self.create_users()

    def create_users(self):
        usernames = ('Mark', 'John', 'Jorge', 'Johny', 'Uri', 'Susan', 'Alex', 'Sarah', 'Alexander', 'Susie', 'Alexey',
                     'Joseph', 'VitaliyC', 'AnjelaC', 'RobertV', 'JosephV', 'VitaliyT', 'AnjelaB', 'RobertR', 'JosephJ',
                     'VitaliyX', 'AnjelaV', 'RobertN', 'JosephS', 'Vitaliy', 'Anjela', 'Robert')
        if Human.objects.count() == 1:
            for el in usernames:

                # self.stdout.write(f'{key}, {val}')
                user = Human(
                    username=f"{el}",
                    is_active=True,
                    is_staff=False,
                    is_superuser=False,
                    )
                user.set_password(el)
                user.save()
            self.stdout.write('Users created')
        else:
            self.stdout.write('Users already exist')
