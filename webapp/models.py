from django.db import models
from .choices import disponible
# Create your models here.
class Doctor(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100,null=True, blank=True)
    sueldo = models.IntegerField(null=True, blank=True)

    def __str__(self):
        text = "{0} {1}"
        return text.format(self.nombre, self.apellido)

class Cliente(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    ci = models.IntegerField()
    prioridad = models.CharField(null=False, blank=False)
    condicion = models.CharField(null=False, blank=False)
    doctor = models.ForeignKey(Doctor, blank=True, null=True, on_delete=models.CASCADE)
    def __str__(self):
        text = "{0} {1}"
        return text.format(self.nombre, self.apellido)
    class Meta:
        ordering = ['prioridad']


class Servicio(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=100)
    sala = models.IntegerField(null=True, blank=True)
    dispobible = models.CharField(null=True, choices=disponible)
    doctor = models.ForeignKey(Doctor, blank=True, null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre