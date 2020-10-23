from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('listar', views.listar, name='listar'),
    path('mostrar_alumnos', views.mostrar_alumnos, name='mostrar_alumnos'),
    path('buscar', views.buscar, name='buscar'),
    path('buscar_por_rut', views.buscar_por_rut, name='buscar_por_rut'),
    path('eliminar', views.eliminar, name='eliminar'),
    path('eliminar_por_rut', views.eliminar_por_rut, name='eliminar_por_rut'),
    path('agregar', views.agregar, name='agregar'),
    path('agregar_alumno', views.agregar_alumno, name='agregar_alumno'),
    path('editar', views.editar, name='editar'),
    path('buscar_para_editar', views.buscar_para_editar, name='buscar_para_editar'),
    path('actualizar_alumno', views.actualizar_alumno, name='actualizar_alumno'),
    path('menu', views.menu, name='menu'),
     path('menu_productos', views.menu_productos, name='menu_productos'),
]

