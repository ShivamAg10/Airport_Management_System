from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.passenger, name="passenger"),
    path("Booking_Flights/", views.Booking_Flights, name="Booking_Flights"),
    path("Search_Results/", views.Search_Results, name="Search_Results"),
    path("Flight_Status/", views.Flight_Status, name="Flight_Status"),
    path("Check_In/", views.Check_In, name="Check_In"),
    path("Booking_History/", views.Booking_History, name="Booking_History"),
    path("Cancellations/", views.Cancellations, name="Cancellations"),
    path("Check_In/Boarding_Pass", views.Boarding_Pass, name="Boarding_Pass"),
]
