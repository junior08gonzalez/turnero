from django.db import models

# Create your models here.

class Cliente(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    ci = models.IntegerField()
    prioridad = models.CharField(null=False, blank=False)
    condicion = models.CharField(null=False, blank=False)

    def __str__(self):
        text = "{0} {1}"
        return text.format(self.nombre, self.apellido)