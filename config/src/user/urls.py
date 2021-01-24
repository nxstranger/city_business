from django.urls import path
from . import views
from django.http import HttpResponse

urlpatterns = [
    path("city/<slug:slug>", views.HumanCityListView.as_view()),
]
