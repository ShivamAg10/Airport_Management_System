from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("Flight_Manager/", views.Flight_Manager, name="Flight_Manager"),
    path("Flight_Manager/FlightInfo", views.FlightInfo, name="FlightInfo"),
    path("Flight_Manager/PlaneInfo", views.PlaneInfo, name="PlaneInfo"),
    path("Flight_Manager/AircraftMaintenance", views.AircraftMaintenance, name="AircraftMaintenance"),
    
    
    path("Flight_Manager/AddAircraft", views.AddAircraft, name="AddAircraft"),
    path("Flight_Manager/ScheduleAircraft", views.ScheduleAircraft, name="ScheduleAircraft"),
    
    path("Crew_Manager/", views.Crew_Manager, name="Crew_Manager"),
    path("Crew_Manager/MissionHub", views.MissionHub, name="MissionHub"),
    path("Crew_Manager/PilotDeck", views.PilotDeck, name="PilotDeck"),
    path("Crew_Manager/HostessDeck", views.HostessDeck, name="HostessDeck"),
    path("Crew_Manager/DutyRoster", views.DutyRoster, name="DutyRoster"),
    path("Crew_Manager/LeaveDesk", views.LeaveDesk, name="LeaveDesk"),
    
    
    path("Crew_Manager/AddPilot", views.AddPilot, name="AddPilot"),
    path("Crew_Manager/AddHostess", views.AddHostess, name="AddHostess"),
]