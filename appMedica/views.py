from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.views.generic.edit import CreateView

# Create your views here.

class PromiseCreateView(CreateView):
    model = Cita
    form_class = registroCitaForm

def about(request):
    return render(request, "about.html", {})

def appointment(request):
    usuario = request.user

    if usuario.is_authenticated:
        citas = registroCitaForm()
        if request.method == "POST":
            citas = registroCitaForm(request.POST)
            if citas.is_valid():
                fechaCita = citas.cleaned_data["fechaCita"]
                horaInicioCita = citas.cleaned_data["horaInicioCita"]
                duracionCita = citas.cleaned_data["duracionCita"]
                medicoCita = Medico.objects.get(rutUsuario = int(request.POST.get("medicoCita")))
                pacienteCita = Perfil.objects.get(user=request.user)
                Cita.objects.create(fechaCita=fechaCita, horaInicioCita=horaInicioCita, duracionCita=duracionCita, medicoCita=medicoCita, pacienteCita=pacienteCita)
                return redirect("home")
    else:
        return redirect("home")

    return render(request, "appointment.html", {"citas": citas})

def blog(request):
    return render(request, "blog.html", {})

def contact(request):
    msj = contactanosForm()
    return render(request, "contact.html", {"msj": msj})

def gallery(request):
    return render(request, "gallery.html", {})

def home(request):
    msj = contactanosForm()
    return render(request, "home.html", {"msj": msj})

def services(request):
    return render(request, "services.html", {})

def team(request):
    return render(request, "team.html", {})

def index(request):
    return render(request, "index.html")

def cerrar_sesion(request):
    logout(request)
    return redirect("home")

def citas(request):
    usuario = request.user
    cita = Cita.objects

    if request.method == "POST":
        if request.POST.get("eliminar"):
            cita.get(id=request.POST["eliminar"]).delete()

    if usuario.is_authenticated:
        citas = Cita.objects.filter(pacienteCita= Perfil.objects.get(user=request.user))
        return render(request, "citas.html", {"citas": citas})
    else:
        return redirect("home")
    