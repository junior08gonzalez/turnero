from django.shortcuts import render, redirect
from .models import Cliente, Servicio
from django.contrib import messages
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# def Inicio(request):
#     return render(request,"index.html")
def salir(request):
    logout(request)
    return redirect('/')

@login_required()
def home(request):
    clientes = Cliente.objects.all()
    # messages.success(request, '!Cupos Limitados!')
    return render(request, 'index.html', {'clientes': clientes})

def registrarCliente(request):
    codigo = request.POST.get('textcodigo',False)
    nombre = request.POST.get('textnombre',False)
    apellido = request.POST.get('textapellido',False)
    ci = request.POST.get('textci',False)
    prioridad = request.POST.get('textprioridad',False)
    condicion = request.POST.get('textcondicion',False)
    cliente = Cliente.objects.create(codigo= codigo, nombre=nombre,apellido=apellido, ci=ci, prioridad=prioridad, condicion=condicion)
    messages.success(request, '!Cliente Registrado!')
    return redirect('/')

def edicionCliente(request, codigo):
    cliente = Cliente.objects.get(codigo= codigo)
    return render(request, 'edicionCliente.html', {'cliente': cliente})

def edicionServicio(request, codigo):
    servicio = Servicio.objects.get(codigo= codigo)
    return render(request, 'edicionServicio.html', {'servicio': servicio})

def editarServicio(request):
    codigo = request.POST.get('textcodigo', False)
    nombre = request.POST.get('textnombre', False)
    sala = request.POST.get('textsala', False)
    disponible = request.POST.get('textdisponible', False)
    servicio = Servicio.objects.get(codigo=codigo)
    servicio.nombre = nombre
    servicio.sala =sala
    # servicio.dispobible = disponible
    servicio.save()
    messages.success(request, '!Servicio Actualizado!')
    return redirect('/')

def editarCliente(request):
    codigo = request.POST.get('textcodigo', False)
    nombre = request.POST.get('textnombre', False)
    apellido = request.POST.get('textapellido', False)
    ci = request.POST.get('textci', False)
    prioridad = request.POST.get('textprioridad', False)
    condicion = request.POST.get('textcondicion', False)
    cliente = Cliente.objects.get(codigo=codigo)
    cliente.nombre = nombre
    cliente.apellido =apellido
    cliente.ci = ci
    cliente.prioridad = prioridad
    cliente.condicion = condicion
    cliente.save()
    messages.success(request, '!Cliente Actualizado!')
    return redirect('/')

def eliminarCliente(request, codigo):
    cliente = Cliente.objects.get(codigo= codigo)
    cliente.delete()
    messages.success(request, '!Cliente Eliminado!')
    return redirect('/')

def ListarServicio(request):
    # nro_servicios = Servicio.objects.count()
    # personas = Persona.objects.all()
    servicios = Servicio.objects.order_by('nombre')
    return render(request, 'listaservicio.html', {'servicios':servicios})