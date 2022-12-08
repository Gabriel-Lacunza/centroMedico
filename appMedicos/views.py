from django.shortcuts import render, redirect
from django.contrib.auth import logout
from appMedica.models import Cita, Medico
from django.utils.timezone import now
from appSecretaria.models import *

# Create your views here.
def homeMed(request):
    return render(request, "indexMed.html", {})

def citasMed(request):
    today = now().date()
    usuario = Medico.objects.get(user = request.user)
    citas = Cita.objects.filter(medicoCita = usuario, fechaCita__gte= today).order_by("fechaCita", "horaInicioCita")
    cantidadCitas = len(citas)
    return render(request, "citasMed.html", {"citas": citas, "cc": cantidadCitas})

def avances(request):
    usuario = Medico.objects.get(user = request.user)
    boletas = Boleta.objects.filter(medico = usuario)
    avanceTotal = 0
    for boleta in boletas:
        avanceTotal += boleta.valorDeLaCita // boleta.comisionDelMedico
    cb = len(boletas)
    return render(request, "avancesMed.html", {"cb":cb, "boletas": boletas, "avance": avanceTotal})

def cerrar_sesion(request):
    logout(request)
    return redirect("home")
