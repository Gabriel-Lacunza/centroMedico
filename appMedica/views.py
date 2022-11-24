from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def about(request):
    return render(request, "about.html", {})

def appointment(request):
    usuario = request.user

    if usuario.is_authenticated:
        print(usuario)
        citas = registroCitaForm()
        if request.method == " POST":
            if citas.is_valid():
                fechaCita = citas.POST.get("fechaCita")
                horaInicioCita = citas.POST.get("horaInicioCita")
                duracionCita = citas.POST.get("duracionCita")
                medicoCita = citas.POST.get("medicoCita")
                Cita.objects.create(fechaCita=fechaCita, horaInicioCita=horaInicioCita, duracionCita=duracionCita, medicoCita=medicoCita)
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

def singIn(request):
    registro = registroUsuarioForm()

    if request.method == "POST":
        if registro.is_valid():
            user= registro.save()
            rut = request.POST.get("rut")
            dv = request.POST.get("dv")
            direccion = request.POST.get("direccion")
            celular = request.POST.get("celular")
            email = request.POST.get("email")
            Perfil.objects.update_or_create(user=user, rut=rut, dv=dv, direccion=direccion, celular=celular, email=email)
            return redirect(home)

    return render(request, "singin.html", {"registro": registro})

def login(request):
    login = loginForm()
    mesg = ""

    if request.method == "POST":
        if login.is_valid:
            nombreDeUsuario = request.POST.get("username")
            nombreDeUsuario = request.POST.get("password")
            user = authenticate(username=nombreDeUsuario, password=nombreDeUsuario)
            if user is not None:
                if user.is_active:
                    login(request, user)
                else:
                    mesg = "¡La cuenta o la password no son correctos!"
            else:
                mesg = "¡La cuenta o la password no son correctos!"
    return render(request, "login.html", {"login": login, "mesg": mesg})

def index(request):
    usuario = request.user
    if not usuario:
        opt = False
    else:
        opt = True
    return render(request, "index.html", {"opt": opt})