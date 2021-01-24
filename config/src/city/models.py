from django.db import models
from ..user.models import Human
# Create your models here.


class City(models.Model):
    """
    """
    name = models.CharField(max_length=150)
    mayor = models.ForeignKey(Human, related_name='mayor', on_delete=models.CASCADE)
    city_motto = models.CharField(max_length=150, default='Life is good')
    citizen = models.ManyToManyField(Human, related_name='citizen')

    def population_multiplier(self):
        """
        :return: <int> multiplication factor for business open calculation
        """
        count = self.citizen.all().count()
        return {

            0 < count < 2: 1,
            2 <= count < 3: 2,
            3 <= count < 5: 3,
            5 <= count < 10: 4,
            10 <= count < 15: 5,
            count >= 15: 10
        }[True]

    def __str__(self):
        return f"{self.name}"

    def population(self):
        if self.citizen.all().count():
            return self.citizen.all().count()
        else:
            return 0


    # def set_citizen(self, human: Human):
    #     """
    #     """
    #     human.citizen = [self]
