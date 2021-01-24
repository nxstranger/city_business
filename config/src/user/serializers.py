from rest_framework import serializers
from .models import Human
from src.business.models import Business


class ListBusinessSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:

        model = Business
        fields = ('id', 'city', 'type')


class ListHumanSerializer(serializers.ModelSerializer):
    """
    """
    citizen = serializers.ReadOnlyField(source="get_citizen")
    business = serializers.ReadOnlyField(source="get_business")
    business_list = ListBusinessSerializer(many=True, read_only=True)

    class Meta:
        model = Human
        fields = ('id', 'username', 'citizen', 'business', 'business_list')

