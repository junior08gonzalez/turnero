from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('salir/', views.salir, name="salir"),
    path('registrarCliente/', views.registrarCliente),
    path('edicionCliente/<codigo>', views.edicionCliente),
    path('listado-servicio/edicionServicio/<codigo>', views.edicionServicio),
    path('editarCliente/', views.editarCliente),
    path('editarServicio/', views.editarServicio),
    path('eliminarCliente/<codigo>', views.eliminarCliente),
    path('listado-servicio/',views.ListarServicio, name="listaservicio"),
]