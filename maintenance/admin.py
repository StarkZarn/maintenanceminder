from django.contrib import admin
from .models import MaintenanceRecord


@admin.register(MaintenanceRecord)
class MaintenanceRecordAdmin(admin.ModelAdmin):
    list_display = ("date", "mileage", "cost", "title", "category")
    search_fields = ("title", "category")
    list_filter = ("category",)
