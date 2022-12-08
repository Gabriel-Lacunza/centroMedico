from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Rol(models.Model):
    nombreRol = models.CharField(max_length=20, unique=True, verbose_name="nombre del rol")

    def __str__(self):
        return self.nombreRol

class Especialidad(models.Model):
    nombreEspecialidad = models.CharField(max_length=30, unique=True, verbose_name="nombre de la especialidad del médico")

    def __str__(self):
        return self.nombreEspecialidad

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rutUsuario = models.IntegerField(primary_key=True, verbose_name="rut(sin digito verificador)")
    dvUsuario = models.CharField(max_length=1, verbose_name="digito verificador")
    nombreUsuario = models.CharField(max_length=30, verbose_name="nombre")
    apellidoUsuario = models.CharField(max_length=30, verbose_name="apellido")
    direccionUsuario = models.CharField(max_length=40, verbose_name="dirrecion")
    telefonoUsuario = models.CharField(max_length=12, verbose_name="telefono celular")
    mailUsuario = models.EmailField(max_length=40, verbose_name="email")
    rolUsuario = models.ForeignKey(Rol, on_delete=models.DO_NOTHING, verbose_name="rol del usuario", default="Paciente")
    especialidadUsuario = models.ForeignKey(Especialidad, on_delete=models.DO_NOTHING, verbose_name="especialidad del medico", null=True, blank=True, default=None)
    
    def __str__(self):
        return f"{self.nombreUsuario} {self.apellidoUsuario} ({self.rutUsuario}-{self.dvUsuario})"

class Medico(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rutUsuario = models.IntegerField(primary_key=True, verbose_name="rut(sin digito verificador)")
    dvUsuario = models.CharField(max_length=1, verbose_name="digito verificador")
    nombreUsuario = models.CharField(max_length=30, verbose_name="nombre")
    apellidoUsuario = models.CharField(max_length=30, verbose_name="apellido")
    direccionUsuario = models.CharField(max_length=40, verbose_name="dirrecion")
    telefonoUsuario = models.CharField(max_length=12, verbose_name="telefono celular")
    mailUsuario = models.EmailField(max_length=40, verbose_name="email")
    especialidadUsuario = models.ForeignKey(Especialidad, on_delete=models.DO_NOTHING, verbose_name="especialidad del medico", default=None)
    
    def __str__(self):
        return f"{self.nombreUsuario} {self.apellidoUsuario} ({self.rutUsuario}-{self.dvUsuario})"

class Cita(models.Model):
    fechaCita = models.DateField(verbose_name="fecha de la cita")
    horaInicioCita = models.TimeField(default=0, verbose_name="hora de la cita")
    duracionCita = models.IntegerField(default=0, verbose_name="duracion aproximada de la cita")
    pacienteCita = models.ForeignKey(Perfil, on_delete=models.DO_NOTHING, related_name="pacienteCita")
    medicoCita = models.ForeignKey(Medico, on_delete=models.DO_NOTHING, related_name="medicoCita", verbose_name="médico para la cita")

    def __str__(self) -> str:
        return f"{self.pacienteCita} (paciente) {self.medicoCita}(médico) - {self.fechaCita}"
