from django.shortcuts import render, redirect
from django.contrib.auth import logout
from appMedica.models import *
from .forms import *
from django.utils.timezone import now

# Create your views here.
def home(request):
    u = request.user.perfil.rolUsuario
    rol = Rol.objects.get(nombreRol = "Secretaria")

    if u != rol:
        return redirect("home")
    return render(request, "indexsec.html", {})

def citasSec(request, act, id):
    today = now().date()
    citas = Cita.objects.all().order_by("fechaCita", "horaInicioCita").filter(fechaCita__gte= today)
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
                return redirect("/sec/citas/crear/-1")
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
                return redirect("/sec/citas/crear/-1")
    elif act == "eliminar":
        citas.get(id = id).delete()
        return redirect("/sec/citas/crear/-1")
        
    return render(request, "citasSec.html", {"citas": citas, "form": form, "cc": cantidadCitas, "act": act, "id": id})

def boletas(request):
    boletas = Boleta.objects.all()
    cantidadBoletas = len(boletas)
    form = BoletaForm()
    
    if request.method == "POST":
        form = BoletaForm(request.POST)
        if form.is_valid():
            cita = form.cleaned_data["cita"]
            valor = form.cleaned_data["valorDeLaCita"]
            comisionMedico = (valor * form.cleaned_data["comisionDelMedico"])/100
            Boleta.objects.create(cita= cita, valorDeLaCita= valor, comisionDelMedico= comisionMedico)
            return redirect("boletas")
    return render(request, "boletasSec.html", { "boletas": boletas ,"cb": cantidadBoletas, "form": form})

def cerrar_sesion(request):
    logout(request)
    return redirect("home")