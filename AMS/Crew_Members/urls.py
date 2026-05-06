from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("Pilot/", views.pilot, name="pilot"),
    path("PIlot/", include("Pilots_Gateways.urls")),
    path("Hostess/", views.Hostess, name="Hostess"),
    path("Hostess/", include("Hostess_Gateways.urls"))
]