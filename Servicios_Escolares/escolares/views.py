from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView

from.models import Alumno
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms
from django.urls import reverse_lazy 

# --------------- ALTAS -------------------------
class CrearAlumno(SuccessMessageMixin, CreateView,LoginRequiredMixin, ListView):
    model = Alumno
    fields = "__all__"
    success_message = "Alumno AGREGADO con EXITO!!"

    def get_success_url(self):
        return reverse('listar')
    
# --------------- BAJAS -------------------------
class EliminarAlumno(DeleteView,LoginRequiredMixin, ListView):
    model = Alumno
    template_name = "alumnos/eliminar.html"

    def get_success_url(self):
        messages.success(self.request, "Alumno ELIMINADO correctamente!!")
        return reverse_lazy('listar')


# --------------- CAMBIOS -------------------------
class ActualizarAlumno(SuccessMessageMixin, UpdateView,LoginRequiredMixin, ListView):
    model = Alumno
    form = Alumno
    fields = "__all__"
    success_message = "Alumno MODIFICADO con EXITO!!"

    def get_success_url(self):
        return reverse('listar')
    
# ---------------  CONSULTAS  -------------------------
class DetalleAlumno(DetailView,LoginRequiredMixin, ListView):
    model = Alumno


class ListarAlumnos(ListView,LoginRequiredMixin):
    model = Alumno

from django.contrib.auth.decorators import login_required

@login_required
def inicio(request):
    return render(request, 'inicio.html')