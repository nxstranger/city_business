from rest_framework import serializers
from src.city.models import City
from src.user.models import Human


class CityUserSerializer(serializers.ModelSerializer):
    """
    smart user info
    """
    username = serializers.ReadOnlyField()

    class Meta:
        model = Human
        fields = ('id', 'username')


class CityModelSerializer(serializers.ModelSerializer):
    """

    """
    city_name = serializers.ReadOnlyField(source='name')
    mayor = CityUserSerializer(many=False, read_only=False)
    citizen = CityUserSerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = ('id', 'city_name', 'mayor', 'population', 'population_multiplier', 'citizen')


class CityListSerializer(serializers.ModelSerializer):
    """
    list get method
    """
    mayor = CityUserSerializer(many=False, read_only=True)
    city_id = serializers.ReadOnlyField(source='id')
    city_name = serializers.ReadOnlyField(source='name')

    class Meta:
        model = City
        fields = ('city_id', 'city_name', 'mayor', 'population')


