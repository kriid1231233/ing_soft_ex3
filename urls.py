from django.urls import path
from . import views

urlpatterns = [
    path('', views.Ferremax, name="Ferremax"),
    path('quienesomos/', views.quienesomos, name="quienesomos"),
    path('contactoForm/', views.contactoForm, name="contactoForm"),
    path('Formularioatencion/', views.Formularioatencion, name="Formularioatencion"),

    path('siguiente/', views.siguiente, name="siguiente"),
    path('crear/', views.crearProducto, name="crear"),
    path('detalle/<id>', views.detalle, name="detalle"),
    path('modificar/<id>/', views.modificar, name="modificar"),
    path('eliminarpro/<id>/', views.eliminar, name="eliminarpro"),

    path('salir/', views.salir, name="salir"),
    path('registrar/', views.registrar, name="registrar"),

    path('tienda/', views.tienda, name="tienda"),

    path('agregar/<id>', views.agregar_producto, name="agregar"),
    path('eliminar/<id>', views.eliminar, name="eliminar"),
    path('restar/<id>', views.restar_producto, name="restar"),
    path('limpiar/', views.limpiar_carrito, name="limpiar"),

    path('generarBoleta/', views.generarBoleta, name="generarBoleta"),
    path('perfil/', views.perfil, name="perfil"),
    
    path('mis-pedidos/', views.mis_pedidos, name='mis_pedidos'),
    path('adminmod/', views.adminmod, name='adminmod'),
    path('guardar_email/', views.guardar_email, name='guardar_email'),
    path('ver_todos_los_pedidos/', views.ver_todos_los_pedidos, name='ver_todos_los_pedidos'),
]

