from django.urls import path
from . import views

urlpatterns = [
    path("", views.maintenance_list, name="maintenance_list"),
    path("<int:pk>/", views.maintenance_detail, name="maintenance_detail"),
    path("new/", views.maintenance_create, name="maintenance_create"),
    path("<int:pk>/edit/", views.maintenance_update, name="maintenance_update"),
    path("<int:pk>/delete/", views.maintenance_delete, name="maintenance_delete"),
]
