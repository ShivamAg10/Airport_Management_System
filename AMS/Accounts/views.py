from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    return render(request, "Accounts/login.html")

def register(request):
    return render(request, "Accounts/register.html")

def profile(request):
    return render(request, "Accounts/profile.html")