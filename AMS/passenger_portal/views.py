from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
def passenger(request):
    return render(request, "passenger_portal/home.html")

@login_required(login_url="login")
def Booking_Flights(request):
    return render(request, "passenger_portal/Booking_Flights.html")

@login_required(login_url="login")
def Search_Results(request):
    return render(request, "passenger_portal/Search_Results.html")

@login_required(login_url="login")
def Flight_Status(request):
    return render(request, "passenger_portal/Flight_Status.html")

@login_required(login_url="login")
def Check_In(request):
    return render(request, "passenger_portal/Check_In.html")

@login_required(login_url="login")
def Booking_History(request):
    return render(request, "passenger_portal/Booking_History.html")

@login_required(login_url="login")
def Cancellations(request):
    return render(request, "passenger_portal/Cancellations.html")

@login_required(login_url="login")
def Boarding_Pass(request):
    return render(request, "passenger_portal/Boarding_Pass.html")