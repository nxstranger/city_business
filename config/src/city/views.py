from rest_framework.generics import ListAPIView
from .models import City
from .serializers import CityListSerializer, CityModelSerializer
from rest_framework import permissions
from src.base import mixins


class ListCityView(ListAPIView):
    """
    """
    serializer_class = CityListSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = City.objects.all().order_by('name')


class CityView(mixins.RetrieveUpdateDestroy):
    """
    """
    serializer_class = CityModelSerializer
    permission_classes = [permissions.IsAdminUser]
    permission_classes_by_action = {'retrieve': [permissions.IsAuthenticated],
                                    'update': [permissions.IsAdminUser],
                                    'destroy': [permissions.IsAdminUser],
                                    }

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        print(pk)
        print(self.request.user)
        print(self.action)
        return City.objects.filter(id=pk)

