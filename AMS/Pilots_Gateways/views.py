from django.shortcuts import render

# Create your views here.
def Documents(request):
    return render(request, "Crew_Members/Pilots/Documents.html")

def Logbook(request):
    return render(request, "Crew_Members/Pilots/Logbook.html")

def Pilot_Roster(request):
    return render(request, "Crew_Members/Pilots/Roster.html")

def Pilot_Safety(request):
    return render(request, "Crew_Members/Pilots/Safety.html")

def Simulations(request):
    return render(request, "Crew_Members/Pilots/Simulations.html")

def Pilot_TakeLeave(request):
    return render(request, "Crew_Members/Pilots/TakeLeave.html")