from django.contrib import admin
from .models import Doctor, Patient, Appointment, Prescription

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("user", "specialization", "phone")

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("user", "age", "phone")

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("date_time", "doctor", "patient", "status")
    list_filter = ("status", "doctor")

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ("appointment", "created_at")
