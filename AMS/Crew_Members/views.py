from django.shortcuts import render

# Create your views here.
def pilot(request):
    return render(request, "Crew_Members/Pilots/home.html")

def Hostess(request):
    return render(request, "Crew_Members/Hostess/home.html")