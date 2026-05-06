from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("Manifest/", views.Manifest, name="Manifest"),
    path("Roster/", views.Roster, name="Roster"),
    path("Safety/", views.Safety, name="Safety"),
    path("Training/", views.Training, name="Training"),
    path("TakeLeave/", views.TakeLeave, name="TakeLeave"),
]