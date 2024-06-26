from django.shortcuts import render, redirect
from .forms import ServiceRecordForm
from .models import ServiceRecord


def index(request):
    records = ServiceRecord.objects.all()
    return render(request, "maintenance/index.html", {"records": records})


def add_record(request):
    if request.method == "POST":
        form = ServiceRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ServiceRecordForm()
    return render(request, "maintenance/add_record.html", {"form": form})


def upcoming_maintenance(request):
    upcoming = ServiceRecord.objects.filter(
        category__name="Regular Maintenance",
        next_service_date__lte=timezone.now()
        + timedelta(days=30),  # example: next service due within 30 days
    )
    return render(request, "maintenance/upcoming.html", {"upcoming": upcoming})
