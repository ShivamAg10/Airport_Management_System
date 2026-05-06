from django.shortcuts import render

# Create your views here.
def Roster(request):
    return render(request, "Crew_Members/Hostess/Roster.html")

def Manifest(request):
    return render(request, "Crew_Members/Hostess/Manifest.html")

def TakeLeave(request):
    return render(request, "Crew_Members/Hostess/TakeLeave.html")

def Safety(request):
    return render(request, "Crew_Members/Hostess/Safety.html")

def Training(request):
    return render(request, "Crew_Members/Hostess/Training.html")