from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("Documents/", views.Documents, name="Documents"),
    path("Logbook/", views.Logbook, name="Logbook"),
    path("Pilot_Roster/", views.Pilot_Roster, name="Pilot_Roster"),
    path("Pilot_Safety/", views.Pilot_Safety, name="Pilot_Safety"),
    path("Simulations/", views.Simulations, name="Simulations"),
    path("Pilot_TakeLeave/", views.Pilot_TakeLeave, name="Pilot_TakeLeave"),
]