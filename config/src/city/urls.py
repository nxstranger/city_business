from django.urls import path
from . import views

urlpatterns = [
    path("", views.ListCityView.as_view()),
    path("<int:pk>", views.CityView.as_view({'get': "retrieve",
                                                    'put': 'update',
                                                    'delete': 'destroy'})),
]
