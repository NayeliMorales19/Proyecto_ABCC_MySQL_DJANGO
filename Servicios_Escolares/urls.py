from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

# ✅ IMPORT CORRECTO
from Servicios_Escolares.escolares import views

urlpatterns = [

    # 🔐 LOGIN COMO PÁGINA PRINCIPAL
    path('', auth_views.LoginView.as_view(
        template_name='registration/login.html'
    ), name='inicio'),

    # 🔐 LOGIN / LOGOUT
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # 🆕 REGISTER
    path('register/', views.register, name='register'),

    # 🛠 ADMIN
    path('admin/', admin.site.urls),

    # 📋 SISTEMA (PROTEGIDO)
    path('alumnos/', views.ListarAlumnos.as_view(), name='listar'),

    # 🔍 DETALLE
    path('alumnos/detalle/<int:pk>/', views.DetalleAlumno.as_view(), name='detalle'),

    # ➕ CREAR
    path('alumnos/crear/', views.CrearAlumno.as_view(), name='crear'),

    # ✏️ EDITAR
    path('alumnos/editar/<int:pk>/', views.ActualizarAlumno.as_view(), name='editar'),

    # ❌ ELIMINAR
    path('alumnos/eliminar/<int:pk>/', views.EliminarAlumno.as_view(), name='eliminar'),
]