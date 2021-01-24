from django.core.management.base import BaseCommand
from src.city.models import City
from src.business.models import Business, BusinessType
from src.business.models import Human
from random import randint

usernames = {
    'Susan': 'Businessmen',
    'Alex': 'Businessmen',
    'Sarah': 'Businessmen',
    'Alexander': 'Businessmen',
    'Susie': 'Businessmen',
    'Alexey': 'Businessmen',
    'Joseph': 'Businessmen',
    'VitaliyC': 'Businessmen',
    'AnjelaC': 'Businessmen',
    'RobertV': 'Businessmen',
    'JosephV': 'Businessmen',
}


class Command(BaseCommand):
    """
    """
    def handle(self, *args, **options):
        """
        """
        self.create_business_types()
        self.create_business()

    def create_business_types(self):
        types = {
            'self-employed': 1,
            'light': 2,
            'medium': 3,
            'hard': 10,
        }

        if BusinessType.objects.count() == 0:
            for key, val in types.items():
                BusinessType.objects.create(
                    category=key,
                    price_multiplier=val
                )
            self.stdout.write('Types created')
        else:
            self.stdout.write('BusinessTypes already exist')

    def create_business(self):
        """
        """
        if (Human.objects.count() < 2 or
                BusinessType.objects.count() == 0 or
                City.objects.count() < 1):
            self.stdout.write('not has relation entities for create Business')
            return False
        if Business.objects.count() == 0:
            city_limit = City.objects.count()
            type_limit = BusinessType.objects.count()
            for name, role in usernames.items():
                bizz = Business(
                    name=f"{name}'s Business",
                    type=BusinessType.objects.all()[randint(0, type_limit-1)],
                    description=f"Business that opened {name}",
                    active=True,
                    city=City.objects.all()[randint(0, city_limit-1)],
                    owner=Human.objects.get(username=name)
                )
                bizz.save()
                if randint(0, 1):
                    bizz = Business(
                        name=f"{name}'s Business",
                        type=BusinessType.objects.all()[randint(0, type_limit - 1)],
                        description=f"Business that opened {name}",
                        active=True,
                        city=City.objects.all()[randint(0, city_limit - 1)],
                        owner=Human.objects.get(username=name)
                    )
                    bizz.save()

            self.stdout.write('Business created')
        else:
            self.stdout.write('Business already exist')
