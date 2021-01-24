from django.core.management.base import BaseCommand
from src.city.models import City
from src.user.models import Human
from random import randint


class Command(BaseCommand):
    """
    """
    def handle(self, *args, **options):
        """
        """
        self.create_users()

    def create_users(self):
        cities = {
            'London': "",
            'Rostov': "",
            'Voronezh': "",
            'Rome': "",
        }

        if City.objects.count() == 0 and Human.objects.count() > 2:
            users = Human.objects.all().order_by('id')[2:]
            gov = Human.objects.get(id=2)
            gov.is_governor = True
            gov.save()
            i = 0
            for key, val in cities.items():

                city = City(
                    name=f"{key}",
                    mayor=users[i],
                    )
                city.save()
                city.citizen.set((users[i],))
                i += 1
            self.stdout.write('Cities created')
            if City.objects.all().count():
                for hum in Human.objects.all().order_by('id')[1:]:
                    city = City.objects.get(id=randint(1, City.objects.all().count()))
                    hum.citizen.set((city,))
            self.stdout.write('Citizen relations installed')
