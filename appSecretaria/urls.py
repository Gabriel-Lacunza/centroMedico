from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="homesec"),
    path("citas/<act>/<id>", citasSec, name="citasSec"),
    path("cerrar", cerrar_sesion, name="cerrar"),
]
