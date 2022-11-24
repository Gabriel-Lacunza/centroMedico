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
    #medicos = ((i["nombreUsuario"], f'{i["nombreUsuario"]}') for i in Perfil.objects.filter(rolUsuario = "Médico").values())
    horas = (
        ("0", "seleccione una opción"),
        ("1", "0:00"),
        ("2", "1:00"),
        ("3", "2:00"),
        ("4", "3:00"),
        ("5", "4:00"),
        ("6", "5:00"),
        ("7", "6:00"),
        ("8", "7:00"),
        ("9", "8:00"),
        ("10", "9:00"),
        ("11", "10:00"),
        ("12", "11:00"),
        ("13", "12:00"),
        ("14", "13:00"),
        ("15", "14:00"),
        ("16", "15:00"),
        ("17", "16:00"),
        ("18", "17:00"),
        ("19", "18:00"),
        ("20", "19:00"),
        ("21", "20:00"),
        ("22", "21:00"),
        ("23", "22:00"),
        ("24", "23:00"),
    )
    duraciones = (
        ("0", "seleccione una opción"),
        ("1", "15 minutos"),
        ("2", "30 minutos"),
        ("3", "45 minutos"),
        ("4", "60 minutos"),
    )
    '''choices= medicos, default=None, .objects.filter(rolUsuario="Médico")'''
    fechaCita = models.DateTimeField(verbose_name="fecha de la cita")
    horaInicioCita = models.TimeField(choices=horas, default=0, verbose_name="hora de la cita")
    duracionCita = models.IntegerField(choices=duraciones, default=0, verbose_name="duracion aproximada de la cita")
    pacienteCita = models.ForeignKey(Perfil, on_delete=models.DO_NOTHING, related_name="pacienteCita")
    medicoCita = models.ForeignKey(Medico, on_delete=models.DO_NOTHING, related_name="medicoCita", verbose_name="médico para la cita")

    def __str__(self) -> str:
        return f"{self.fechaCita} - paciente: {self.pacienteCita} con medico: {self.medicoCita}"

class Boleta(models.Model):
    idCitaBoleta = models.IntegerField()
    fechaEmisionBoleta = models.DateTimeField(auto_now_add=True)
    valorBrutoBoleta = models.IntegerField()
    valorNetoBoleta = models.IntegerField()
    comisionMedicaBoleta = models.IntegerField()