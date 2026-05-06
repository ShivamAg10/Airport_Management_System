from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("Public_Access.urls")),
    path("passenger/", include("passenger_portal.urls")),
    path("accounts/", include('Accounts.urls')),
    path("Crew/", include("Crew_Members.urls")),
    path("Management/", include("Management.urls")),
]