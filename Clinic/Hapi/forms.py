from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Custom user model storing only email, role, and fhir_id

# Base User Registration Form (Only for authentication)
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']

# Doctor Registration Form (Only for FHIR data)
class DoctorRegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    phone = forms.CharField(max_length=15, required=True)
    date_of_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')], required=True)
    specialty = forms.CharField(max_length=100, required=True)
    license_number = forms.CharField(max_length=50, required=True)

# Patient Registration Form (Only for FHIR data)
class PatientRegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    phone = forms.CharField(max_length=15, required=True)
    date_of_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')], required=True)
    address = forms.CharField(max_length=255, required=True)

class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)