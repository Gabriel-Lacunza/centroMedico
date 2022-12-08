from django.shortcuts import render, redirect
from .forms import registroUsuarioForm
from appMedica.models import Perfil
# Create your views here.
def register(request):
    form = registroUsuarioForm()

    if request.method == "POST":
        form = registroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            rut = request.POST.get("rut")
            dv = request.POST.get("dv")
            nombre = request.POST.get("nombre")
            apellido = request.POST.get("apellido")
            direccion = request.POST.get("direccion")
            celular = request.POST.get("celular")
            email = request.POST.get("email")
            Perfil.objects.create(user = user, rutUsuario = rut, dvUsuario = dv, nombreUsuario = nombre, 
            apellidoUsuario = apellido, direccionUsuario = direccion, telefonoUsuario = celular, mailUsuario = email)
            return redirect("home")

    return render(request, "register/register.html", {"form": form})