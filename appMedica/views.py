from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
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
    u = request.user
    rol = Rol.objects
    
    if u.is_authenticated:
        try:
            usuario = Perfil.objects.get(user = u)
            if usuario.rolUsuario == rol.get(nombreRol= "Secretaria"):
                return redirect("sec/")
            elif usuario.rolUsuario == rol.get(nombreRol= "Médico"):
                return redirect("med/")
        except:
            pass
    return render(request, "home.html", {"msj": msj})

def loginV(request):
    loginvar = AuthenticationForm()

    if request.method == "POST":
        loginvar = AuthenticationForm(request, data=request.POST)

        if loginvar.is_valid():
            nombre = request.POST.get("username")
            contrasenna = request.POST.get("password")
            usuario = authenticate(request, username= nombre, password= contrasenna)
            u = Perfil.objects.get(user = usuario).rolUsuario
            rol = Rol.objects.get(nombreRol=u)

            if usuario is not None:
                if usuario.is_active:
                    login(request, usuario)
                    if rol == Rol.objects.get(nombreRol="Paciente"):
                        return redirect("home")
                    elif rol == Rol.objects.get(nombreRol="Secretaria"):
                        return redirect("sec/")
                    elif rol == Rol.objects.get(nombreRol= "Médico"):
                        return redirect("med/")
                            
    return render(request, "login.html", {"login": loginvar})

def services(request):
    return render(request, "services.html", {})

def team(request):
    return render(request, "team.html", {})

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
    