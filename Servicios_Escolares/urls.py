from django.contrib import admin
from django.urls import path
from Servicios_Escolares.escolares.views import *

urlpatterns = [
    # INICIO (evita error 404 en /)
    path('', ListarAlumnos.as_view(
        template_name="alumnos/index.html"
    ), name='inicio'),

    path('admin/', admin.site.urls),

    # LISTAR
    path('alumnos/', ListarAlumnos.as_view(
        template_name="alumnos/index.html"
    ), name='listar'),

    # DETALLE
    path('alumnos/detalle/<int:pk>/', DetalleAlumno.as_view(
        template_name="alumnos/detalle.html"
    ), name='detalle'),

    # CREAR
    path('alumnos/crear/', CrearAlumno.as_view(
        template_name="alumnos/crear.html"
    ), name='crear'),

    # EDITAR
    path('alumnos/editar/<int:pk>/', ActualizarAlumno.as_view(
        template_name="alumnos/editar.html"
    ), name='editar'),

    # ELIMINAR
    path('alumnos/eliminar/<int:pk>/', EliminarAlumno.as_view(), name='eliminar'),
]