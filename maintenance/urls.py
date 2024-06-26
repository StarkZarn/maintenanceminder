from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_record, name="add_record"),
    path("upcoming/", views.upcoming_maintenance, name="upcoming_maintenance"),
]
