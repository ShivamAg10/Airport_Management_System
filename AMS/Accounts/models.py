from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import UserManager
from django.utils.translation import gettext_lazy
from django.contrib.auth.hashers import check_password, make_password

class CustomUser(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = (
        ('passenger', 'Passenger'),
        ('crew', 'Flight Crew'),
        ('manager', 'Manager'),
        ('superadmin', 'Super Admin'),
    )

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['first_name', 'last_name']
    
    def __str__(self):
        return f"{self.email} ({self.user_type})"

# 3. Passenger Class (Inherits everything from CustomUser)
class Passenger(CustomUser):
    passport_number = models.CharField(max_length=30, unique=True)
    aadhar_number = models.CharField(max_length=12, unique=True)
    nationality = models.CharField(max_length=50)
    date_of_birth = models.DateField()

# 4. Crew Class (Pilots & Hostesses)
class Crew(CustomUser):
    ROLE_CHOICES = (
        ('pilot', 'Pilot'),
        ('hostess', 'Flight Attendant'),
    )
    employee_id = models.CharField(max_length=10, unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    license_number = models.CharField(max_length=50, blank=True)
    total_flight_hours = models.PositiveIntegerField(default=0)

# 5. Manager Class
class Manager(CustomUser):
    DEPT_CHOICES = (
        ('crew_manager', 'Crew Manager'),
        ('flight_manager', 'Flight Manager'),
    )
    department = models.CharField(max_length=20, choices=DEPT_CHOICES)