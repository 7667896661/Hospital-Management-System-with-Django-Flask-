from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Doctor, Patient, Appointment, Prescription
from .forms import UserRegistrationForm, AppointmentForm, PrescriptionForm
from django.contrib import messages

def home(request):
    upcoming = Appointment.objects.filter(status="SCHEDULED").order_by("date_time")[:5]
    return render(request, "core/home.html", {"upcoming": upcoming})

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, "core/doctor_list.html", {"doctors": doctors})

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, "core/patient_list.html", {"patients": patients})

@login_required
def appointment_list(request):
    # if staff show all, else show patient or doctor filtered
    if request.user.is_staff:
        appts = Appointment.objects.all().order_by("-date_time")
    else:
        appts = Appointment.objects.filter(patient__user=request.user) | Appointment.objects.filter(doctor__user=request.user)
    appts = appts.distinct()
    return render(request, "core/appointment_list.html", {"appointments": appts})

@login_required
def appointment_create(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Appointment scheduled.")
            return redirect("core:appointment_list")
    else:
        form = AppointmentForm()
    return render(request, "core/appointment_form.html", {"form": form})

@login_required
def appointment_detail(request, pk):
    appt = get_object_or_404(Appointment, pk=pk)
    return render(request, "core/appointment_detail.html", {"appointment": appt})

@login_required
def prescription_create(request, appt_pk):
    appt = get_object_or_404(Appointment, pk=appt_pk)
    if request.method == "POST":
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            pres = form.save(commit=False)
            pres.appointment = appt
            pres.save()
            messages.success(request, "Prescription saved.")
            return redirect("core:appointment_detail", pk=appt_pk)
    else:
        form = PrescriptionForm()
    return render(request, "core/prescription_form.html", {"form": form, "appointment": appt})

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request, user)
            messages.success(request, "Account created.")
            return redirect("core:home")
    else:
        form = UserRegistrationForm()
    return render(request, "core/register.html", {"form": form})
