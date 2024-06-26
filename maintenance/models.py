from django.db import models
from django.utils import timezone
from datetime import timedelta


class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ServiceRecord(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    odometer_reading = models.PositiveIntegerField()
    next_service_mileage = models.PositiveIntegerField(null=True, blank=True)
    next_service_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.category.name == "Regular Maintenance":
            if not self.next_service_mileage:
                self.next_service_mileage = (
                    self.odometer_reading + 5000
                )  # example value for next service mileage
            if not self.next_service_date:
                self.next_service_date = self.date + timedelta(
                    days=180
                )  # example value for next service date
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} on {self.date}"
