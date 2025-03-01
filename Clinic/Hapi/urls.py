from django.urls import path
from . import views

app_name = 'Hapi'  # This defines the app namespace

urlpatterns = [
    path('/', views.landing_page, name='landing_page'),  # Landing page URL
    path('/register/<str:role>/', views.register, name='register'),
    path('/login/', views.user_login, name='login'),
    path('/user_dashboard/', views.user_dashboard, name='dashboard'),
    path('/profile/doctor/', views.doctor_profile, name='doctor_profile'),
    path('/logout/', views.user_logout, name='logout'),

    #Appointment
    path("/pending-appointments/", views.pending_appointments, name="pending_appointments"),
]
