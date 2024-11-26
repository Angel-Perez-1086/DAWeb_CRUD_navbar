from django.urls import path
from . import views
urlpatterns = [
    path('clientes',views.inicio_vistaClientes,name='clientes'),
    path('registrarCliente/',views.registrarCliente, name='registrarCliente'),
    path('seleccionarCliente/<id_cliente>',views.seleccionarCliente,name="seleccionarClinte"),
    path('editarCliente/',views.editarCliente,name="editarCliente"),
    path("borrarCliente/<id_cliente>",views.borrarCliente,name="borrarCliente")
]