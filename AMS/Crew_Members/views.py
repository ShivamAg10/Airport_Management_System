from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
def pilot(request):
    return render(request, "Crew_Members/Pilots/home.html")

@login_required(login_url="login")
def Hostess(request):
    return render(request, "Crew_Members/Hostess/home.html")