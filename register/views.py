from django.shortcuts import render, redirect
from .forms import registroUsuarioForm
# Create your views here.
def register(request):
    form = registroUsuarioForm()

    if request.method == "POST":
        form = registroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    return render(request, "register/register.html", {"form": form})