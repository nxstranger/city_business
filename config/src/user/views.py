from rest_framework.generics import ListAPIView, GenericAPIView
from .serializers import ListHumanSerializer
from .models import Human
from src.city.models import City
from rest_framework import permissions
from .pagination import StandardResultsSetPagination
# Create your views here.


class HumanCityListView(ListAPIView):
    serializer_class = ListHumanSerializer
    # queryset = Human.objects.all().order_by('id')
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self, slug=''):
        slug = str(self.kwargs.get('slug', None)).capitalize()
        queryset = []
        city = City.objects.filter(name=slug)
        # print(f'{slug}')
        if city:
            queryset = Human.objects.filter(citizen=city[0])
        return queryset
