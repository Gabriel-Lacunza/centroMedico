from email.policy import default
from django import forms
from django.forms import ModelForm, fields, Form
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

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

class loginForm(Form):
    nombreDeUsuario = forms.CharField(widget=forms.TextInput(), label="Nombre")
    passwordUsuario = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")

    class Meta:
        fields = ["nombreDeUsuario", "passwordUsuario"]

class registroCitaForm(ModelForm):
    class Meta:
        model = Cita
        fields = [
            "fechaCita",
            "horaInicioCita",
            "duracionCita",
            "medicoCita"
        ]
        widgets = {
            'fechaCita': DateInput(),
            'horaInicioCita': TimeInput()
        }

class modificacionUsuarioForm(UserCreationForm):
    nombre = forms.CharField(max_length=30, min_length=5)
    apellido = forms.CharField(max_length=30, min_length=10)
    direccion = forms.CharField(max_length=30, min_length=10)
    celular = forms.IntegerField(max_value=10000000000, min_value=99999999999, label="telefono celular (con codigo de área)")
    email = forms.EmailField(max_length=40)
    class Meta:
        model = User 
        fields = [
            "nombre",
            "apellido",
            "direccion",
            "celular",
            "email"
        ]

class contactanosForm(Form):
    nombre = forms.CharField(max_length=30, min_length=5)
    email = forms.EmailField(max_length=40)
    telefonoCelular = forms.CharField(label="Numero de telefono")
    mensaje = forms.CharField(widget=forms.Textarea())

class registroRol(ModelForm):
    class Meta:
        model = Rol
        fields = ["nombreRol"]

class registroEspecialidad(ModelForm):
    class Meta:
        model = Especialidad
        fields = ["nombreEspecialidad"]