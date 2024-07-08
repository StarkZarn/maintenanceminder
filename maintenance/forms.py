# maintenance/forms.py

from django import forms
from .models import MaintenanceRecord


class MaintenanceRecordForm(forms.ModelForm):
    class Meta:
        model = MaintenanceRecord
        fields = ["date", "mileage", "cost", "title", "category", "note"]
        widgets = {
            "date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "mileage": forms.NumberInput(attrs={"class": "form-control"}),
            "cost": forms.NumberInput(attrs={"class": "form-control"}),
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "note": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }
