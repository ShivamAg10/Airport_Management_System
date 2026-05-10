from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
def Documents(request):
    return render(request, "Crew_Members/Pilots/Documents.html")

@login_required(login_url="login")
def Logbook(request):
    return render(request, "Crew_Members/Pilots/Logbook.html")

@login_required(login_url="login")
def Pilot_Roster(request):
    return render(request, "Crew_Members/Pilots/Roster.html")

@login_required(login_url="login")
def Pilot_Safety(request):
    return render(request, "Crew_Members/Pilots/Safety.html")

@login_required(login_url="login")
def Simulations(request):
    return render(request, "Crew_Members/Pilots/Simulations.html")

@login_required(login_url="login")
def Pilot_TakeLeave(request):
    return render(request, "Crew_Members/Pilots/TakeLeave.html")