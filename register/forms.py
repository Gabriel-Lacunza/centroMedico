from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class registroUsuarioForm(UserCreationForm):
    rut = forms.IntegerField(max_value=10000000, min_value=99999999)
    dv = forms.CharField(max_length=1)
    nombre = forms.CharField(max_length=30, min_length=10)
    apellido = forms.CharField(max_length=30, min_length=10)
    direccion = forms.CharField(max_length=30, min_length=10)
    celular = forms.IntegerField(max_value=10000000000, min_value=99999999999, label="telefono celular (con codigo de área)")
    email = forms.EmailField(max_length=40)
    class Meta:
        model = User 
        fields = [
            "rut",
            "dv",
            "nombre",
            "apellido",
            "direccion",
            "celular",
            "email"
        ]