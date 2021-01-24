from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Human(AbstractUser):
    """
    """
    is_governor = models.BooleanField(default=False)
    cash = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.username}'

    def is_citizen(self):
        relations = ""
        if self.citizen.all():
            relations += f"citizen: "
            for el in self.citizen.all():
                relations += f'{el.name} '
        return relations

    def is_mayor(self):
        if self.mayor.all():
            return self.mayor.all()[0].name

    def get_business(self):
        relations = ""
        if self.business_owner.all():
            relations += f"business: "
            for el in self.business_owner.all():
                relations += f'{el.city} '
        return relations

    def business_list(self):
        return self.business_owner.all()
