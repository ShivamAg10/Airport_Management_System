from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
def Roster(request):
    return render(request, "Crew_Members/Hostess/Roster.html")

@login_required(login_url="login")
def Manifest(request):
    return render(request, "Crew_Members/Hostess/Manifest.html")

@login_required(login_url="login")
def TakeLeave(request):
    return render(request, "Crew_Members/Hostess/TakeLeave.html")

@login_required(login_url="login")
def Safety(request):
    return render(request, "Crew_Members/Hostess/Safety.html")

@login_required(login_url="login")
def Training(request):
    return render(request, "Crew_Members/Hostess/Training.html")