from django.urls import path
from .views import *

urlpatterns = [
    path("", homeMed, name="homeMed"),
    path("citas", citasMed, name="citasMed"),
    path("avances", avances, name="avances"),
]
