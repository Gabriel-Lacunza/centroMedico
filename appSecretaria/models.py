from django.db import models
from appMedica.models import Cita, Medico

# Create your models here.

class Boleta(models.Model):
    cita = models.ForeignKey(Cita, models.DO_NOTHING, default= None)
    fechaEmisionBoleta = models.DateField(auto_now_add=True)
    valorDeLaCita = models.IntegerField(verbose_name="Valor de la cita")
    comisionDelMedico = models.IntegerField(verbose_name="Porcentaje que se lleva el médico")
    medico = models.ForeignKey(Medico, models.DO_NOTHING, default= None)