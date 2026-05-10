from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login")
def Flight_Manager(request):
    return render(request, "Management/Flight_Manager/home.html")

@login_required(login_url="login")
def FlightInfo(request):
    return render(request, "Management/Flight_Manager/FlightInfo.html")

@login_required(login_url="login")
def PlaneInfo(request):
    return render(request, "Management/Flight_Manager/PlaneInfo.html")

@login_required(login_url="login")
def AircraftMaintenance(request):
    return render(request, "Management/Flight_Manager/AircraftMaintenance.html")

@login_required(login_url="login")
def AddAircraft(request):
    return render(request, "Management/Flight_Manager/AddAircraft.html")

@login_required(login_url="login")
def ScheduleAircraft(request):
    return render(request, "Management/Flight_Manager/ScheduleAircraft.html")



@login_required(login_url="login")
def Crew_Manager(request):
    return render(request, "Management/Crew_Manager/home.html")

@login_required(login_url="login")
def MissionHub(request):
    return render(request, "Management/Crew_Manager/MissionHub.html")

@login_required(login_url="login")
def PilotDeck(request):
    return render(request, "Management/Crew_Manager/PilotDeck.html")

@login_required(login_url="login")
def AddPilot(request):
    return render(request, "Management/Crew_Manager/AddPilot.html")

@login_required(login_url="login")
def HostessDeck(request):
    return render(request, "Management/Crew_Manager/HostessDeck.html")

@login_required(login_url="login")
def AddHostess(request):
    return render(request, "Management/Crew_Manager/AddHostess.html")

@login_required(login_url="login")
def DutyRoster(request):
    return render(request, "Management/Crew_Manager/DutyRoster.html")

@login_required(login_url="login")
def LeaveDesk(request):
    return render(request, "Management/Crew_Manager/LeaveDesk.html")