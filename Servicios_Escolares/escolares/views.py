from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Alumno
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# 🔹 LISTAR
class ListarAlumnos(LoginRequiredMixin, ListView):
    model = Alumno
    template_name = "alumnos/index.html"


# 🔹 DETALLE
class DetalleAlumno(LoginRequiredMixin, DetailView):
    model = Alumno
    template_name = "alumnos/detalle.html"
    context_object_name = "alumno"


# 🔹 CREAR
from django.contrib import messages

class CrearAlumno(LoginRequiredMixin, CreateView):
    model = Alumno
    fields = "__all__"
    template_name = "alumnos/crear.html"

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Alumno agregado correctamente")
        return self.render_to_response(self.get_context_data(form=form))


# 🔹 EDITAR
from django.contrib import messages

class ActualizarAlumno(LoginRequiredMixin, UpdateView):
    model = Alumno
    fields = "__all__"
    template_name = "alumnos/editar.html"

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Alumno modificado correctamente")
        return self.render_to_response(self.get_context_data(form=form))


# 🔹 ELIMINAR
class EliminarAlumno(LoginRequiredMixin, DeleteView):
    model = Alumno
    template_name = "alumnos/eliminar.html"

    def get_success_url(self):
        messages.success(self.request, "Alumno ELIMINADO correctamente!!")
        return reverse_lazy('listar')


# 🔹 INICIO PROTEGIDO
from django.contrib.auth.decorators import login_required

@login_required
def inicio(request):
    return render(request, 'inicio.html')


# 🔹 REGISTRO
def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request, 'registration/register.html', {'form': form})