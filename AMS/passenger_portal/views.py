from django.shortcuts import render

# Create your views here.

def passenger(request):
    return render(request, "passenger_portal/home.html")

def Booking_Flights(request):
    return render(request, "passenger_portal/Booking_Flights.html")

def Search_Results(request):
    return render(request, "passenger_portal/Search_Results.html")

def Flight_Status(request):
    return render(request, "passenger_portal/Flight_Status.html")

def Check_In(request):
    return render(request, "passenger_portal/Check_In.html")

def Booking_History(request):
    return render(request, "passenger_portal/Booking_History.html")

def Cancellations(request):
    return render(request, "passenger_portal/Cancellations.html")

def Boarding_Pass(request):
    return render(request, "passenger_portal/Boarding_Pass.html")