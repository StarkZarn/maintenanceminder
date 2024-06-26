from django import forms
from .models import ServiceRecord


class ServiceRecordForm(forms.ModelForm):
    class Meta:
        model = ServiceRecord
        fields = [
            "name",
            "date",
            "time",
            "cost",
            "odometer_reading",
            "category",
            "next_service_mileage",
            "next_service_date",
        ]
