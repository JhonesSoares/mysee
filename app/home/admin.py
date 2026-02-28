from django.contrib import admin

# Register your models here.
from .models import About, Services


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin): ...


@admin.register(About)
class AboutAdmin(admin.ModelAdmin): ...
