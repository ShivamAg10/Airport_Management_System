from django.contrib import admin
from .models import CustomUser, Passenger, Crew, Manager

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'user_type', 'is_staff')
    list_filter = ('user_type', 'is_staff', 'is_active')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('date_joined',)

@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    # Note: You can pull fields from the parent (CustomUser) into this display!
    list_display = ('email', 'first_name', 'last_name', 'passport_number', 'nationality')
    search_fields = ('email', 'passport_number', 'aadhar_number')

# 3. Crew Admin
@admin.register(Crew)
class CrewAdmin(admin.ModelAdmin):
    list_display = ('email', 'employee_id', 'role', 'license_number', 'total_flight_hours')
    list_filter = ('role',)
    search_fields = ('email', 'employee_id', 'license_number')

# 4. Manager Admin
@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('email', 'department')
    list_filter = ('department',)