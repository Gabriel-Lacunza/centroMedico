from django.shortcuts import render, redirect
from django.contrib.auth import logout
from appMedica.models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, "indexsec.html", {})

def citasSec(request, act, id):
    citas = Cita.objects.all()
    cantidadCitas = len(citas)
    form = registroCitaFormSec()

    if act == "crear":
        if request.method == "POST":
            form = registroCitaFormSec(request.POST)
            if form.is_valid():
                fechaCita = form.cleaned_data["fechaCita"]
                horaInicioCita = form.cleaned_data["horaInicioCita"]
                duracionCita = form.cleaned_data["duracionCita"]
                medicoCita = Medico.objects.get(rutUsuario = int(request.POST.get("medicoCita")))
                pacienteCita = Perfil.objects.get(rutUsuario = int(request.POST.get("pacienteCita")))
                Cita.objects.create(fechaCita=fechaCita, horaInicioCita=horaInicioCita, duracionCita=duracionCita, medicoCita=medicoCita, pacienteCita=pacienteCita)
    elif act == "editar":
        objeto = citas.get(id = id)
        form = registroCitaFormSec(instance=objeto)
        if request.method == "POST":
            form = registroCitaFormSec(request.POST)
            if form.is_valid():
                objeto.fechaCita = form.cleaned_data["fechaCita"]
                objeto.horaInicioCita = form.cleaned_data["horaInicioCita"]
                objeto.duracionCita = form.cleaned_data["duracionCita"]
                objeto.medicoCita = Medico.objects.get(rutUsuario = int(request.POST.get("medicoCita")))
                objeto.pacienteCita = Perfil.objects.get(rutUsuario = int(request.POST.get("pacienteCita")))
                objeto.save()
    elif act == "eliminar":
        citas.get(id = id).delete()
        
    return render(request, "citasSec.html", {"citas": citas, "form": form, "cc": cantidadCitas, "act": act, "id": id})

def cerrar_sesion(request):
    logout(request)
    return redirect("home")