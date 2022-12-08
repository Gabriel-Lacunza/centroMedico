from appMedica.models import Cita
from django import forms
from django.forms import ModelForm, Form
from .models import Boleta

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'


class registroCitaFormSec(ModelForm):
    class Meta:
        model = Cita
        fields = [
            "fechaCita",
            "horaInicioCita",
            "duracionCita",
            "pacienteCita",
            "medicoCita"
        ]
        widgets = {
            'fechaCita': DateInput(),
            'horaInicioCita': TimeInput()
        }

class BoletaForm(ModelForm):
    comisionDelMedico = forms.IntegerField(max_value=100)
    class Meta:
        model = Boleta
        fields = [
            "cita",
            "valorDeLaCita",
            "comisionDelMedico"
        ]