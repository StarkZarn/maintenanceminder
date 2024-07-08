from django.shortcuts import render, get_object_or_404, redirect
from .models import MaintenanceRecord
from .forms import MaintenanceRecordForm


def maintenance_list(request):
    records = MaintenanceRecord.objects.all()
    return render(request, "maintenance/maintenance_list.html", {"records": records})


def maintenance_detail(request, pk):
    record = get_object_or_404(MaintenanceRecord, pk=pk)
    return render(request, "maintenance/maintenance_detail.html", {"record": record})


def maintenance_create(request):
    if request.method == "POST":
        form = MaintenanceRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("maintenance_list")
    else:
        form = MaintenanceRecordForm()
    return render(request, "maintenance/maintenance_form.html", {"form": form})


def maintenance_update(request, pk):
    record = get_object_or_404(MaintenanceRecord, pk=pk)
    if request.method == "POST":
        form = MaintenanceRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect("maintenance_list")
    else:
        form = MaintenanceRecordForm(instance=record)
    return render(request, "maintenance/maintenance_form.html", {"form": form})


def maintenance_delete(request, pk):
    record = get_object_or_404(MaintenanceRecord, pk=pk)
    if request.method == "POST":
        record.delete()
        return redirect("maintenance_list")
    return render(
        request, "maintenance/maintenance_confirm_delete.html", {"record": record}
    )
