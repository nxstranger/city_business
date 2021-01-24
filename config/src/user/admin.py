from django.contrib import admin
from .models import Human


@admin.register(Human)
class HumanAdmin(admin.ModelAdmin):
    """
    """
    list_display = 'id', 'username', 'is_citizen', 'is_mayor', 'get_business', 'is_governor'
