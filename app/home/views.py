from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import About, Services


def home(request: HttpRequest) -> HttpResponse:
    abouts = About.objects.all().order_by("id")
    return render(request, "home/pages/home.html", context={"abouts": abouts})


def services(request: HttpRequest) -> HttpResponse:
    services = Services.objects.all().order_by("id")
    return render(request, "home/pages/services.html", context={"services": services})
