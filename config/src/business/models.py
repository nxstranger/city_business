from django.db import models
from ..user.models import Human
from ..city.models import City
# Create your models here.


def multiplier_validator(model):
    return False if model.price_multiplier > 10 or model.price_multiplier < 1 else True


class BusinessType(models.Model):
    """
    """
    category = models.CharField(max_length=50, unique=True, null=False)
    price_multiplier = models.PositiveIntegerField(validators=[multiplier_validator], null=False)

    def open_business_price(self, city: City):
        return city.population_multiplier * self.price_multiplier

    def __str__(self):
        return self.category


class Business(models.Model):
    """
    """
    name = models.CharField(max_length=50)
    type = models.ForeignKey(BusinessType, related_name='business_type', on_delete=models.CASCADE)
    description = models.CharField(max_length=150)
    active = models.BooleanField(default=True)
    city = models.ForeignKey(City, related_name='business_city', on_delete=models.CASCADE)
    owner = models.ForeignKey(Human, related_name='business_owner', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.owner} {self.city} {self.type}"
