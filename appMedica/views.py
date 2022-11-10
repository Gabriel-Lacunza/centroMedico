from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about(request):
    return render(request, "about.html", {})

def appointment(request):
    return render(request, "appointment.html", {})

def blog(request):
    return render(request, "blog.html", {})

def contact(request):
    return render(request, "contact.html", {})

def gallery(request):
    return render(request, "gallery.html", {})

def home(request):
    return render(request, "home.html", {})

def services(request):
    return render(request, "services.html", {})

def team(request):
    return render(request, "team.html", {})