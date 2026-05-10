from django.shortcuts import render, redirect
from .models import CustomUser, Passenger
from django.contrib import messages, auth

# Create your views here.
def login(request):
    
    return render(request, "Accounts/login.html")

def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        date_of_birth = request.POST.get("date_of_birth")
        aadhar_number = request.POST.get("aadhar_number")
        nationality = request.POST.get("nationality")
        passport_number = request.POST.get("passport_number")
        
        # print(first_name, last_name, email, phone_number, date_of_birth, aadhar_number, nationality, passport_number)
        
        try:
            new_user = Passenger.objects.create(
                first_name = first_name,
                last_name = last_name,
                email = email,
                phone_number = phone_number,
                date_of_birth = date_of_birth,
                aadhar_number = aadhar_number,
                nationality = nationality,
                passport_number = passport_number,
                user_type = "passenger",
            )
        
            if password == confirm_password:
                new_user.set_password(password)
                new_user.save()
                messages.success(request, "Registeration Successfull")
                return redirect('login')
            else:
                messages.error(request, "Password and Confirm Password is not same")
                return redirect('/')
        except:
            messages.error(request, "Something went wrong!!!")
            return redirect('register')
    return render(request, "Accounts/register.html")

def profile(request):
    return render(request, "Accounts/profile.html")