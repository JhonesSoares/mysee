from django.urls import path

from . import views

app_name = "home"

urlpatterns = [
    path("", views.home, name="home"),
    path("services", views.services, name="services"),
    # path("projeto/<int:id>/", views.project, name="projeto"),
]
