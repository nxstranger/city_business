from django.contrib import admin
from .models import Business, BusinessType


@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    """
    """
    list_display = 'id', 'owner', 'city', 'active'
    ordering = 'id',


@admin.register(BusinessType)
class BusinessTypeAdmin(admin.ModelAdmin):
    """
    """