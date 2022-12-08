from appMedica.models import Cita
from django import forms
from django.forms import ModelForm, Form


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