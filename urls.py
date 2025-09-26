from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("doctors/", views.doctor_list, name="doctor_list"),
    path("patients/", views.patient_list, name="patient_list"),
    path("appointments/", views.appointment_list, name="appointment_list"),
    path("appointments/new/", views.appointment_create, name="appointment_create"),
    path("appointment/<int:pk>/", views.appointment_detail, name="appointment_detail"),
    path("prescription/<int:appt_pk>/add/", views.prescription_create, name="prescription_create"),
    path("register/", views.register, name="register"),
]
