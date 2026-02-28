from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import About


def home(request: HttpRequest) -> HttpResponse:
    abouts = About.objects.all().order_by("id")
    return render(request, "home/pages/home.html", context={"abouts": abouts})
