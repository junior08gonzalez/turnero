from django.contrib import admin
from . models import Cliente, Servicio, Doctor
# Register your models here.
admin.site.register(Cliente),
admin.site.register(Servicio),
admin.site.register(Doctor),