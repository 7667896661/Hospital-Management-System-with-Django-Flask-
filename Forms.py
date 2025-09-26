from django import forms
from django.contrib.auth.models import User
from .models import Appointment, Prescription

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password")

class AppointmentForm(forms.ModelForm):
    date_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"type":"datetime-local"}))
    class Meta:
        model = Appointment
        fields = ("doctor", "patient", "date_time", "reason")

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ("notes", "medicines")
