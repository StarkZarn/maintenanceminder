from django.db import models


class MaintenanceRecord(models.Model):
    CATEGORY_CHOICES = [
        ("repair", "Repair"),
        ("preventative", "Preventative"),
    ]

    date = models.DateField()
    mileage = models.PositiveIntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
