from django.shortcuts import render

# Create your views here.

def Flight_Manager(request):
    return render(request, "Management/Flight_Manager/home.html")

def FlightInfo(request):
    return render(request, "Management/Flight_Manager/FlightInfo.html")

def PlaneInfo(request):
    return render(request, "Management/Flight_Manager/PlaneInfo.html")

def AircraftMaintenance(request):
    return render(request, "Management/Flight_Manager/AircraftMaintenance.html")

def AddAircraft(request):
    return render(request, "Management/Flight_Manager/AddAircraft.html")

def ScheduleAircraft(request):
    return render(request, "Management/Flight_Manager/ScheduleAircraft.html")




def Crew_Manager(request):
    return render(request, "Management/Crew_Manager/home.html")

def MissionHub(request):
    return render(request, "Management/Crew_Manager/MissionHub.html")

def PilotDeck(request):
    return render(request, "Management/Crew_Manager/PilotDeck.html")

def AddPilot(request):
    return render(request, "Management/Crew_Manager/AddPilot.html")

def HostessDeck(request):
    return render(request, "Management/Crew_Manager/HostessDeck.html")

def AddHostess(request):
    return render(request, "Management/Crew_Manager/AddHostess.html")

def DutyRoster(request):
    return render(request, "Management/Crew_Manager/DutyRoster.html")

def LeaveDesk(request):
    return render(request, "Management/Crew_Manager/LeaveDesk.html")