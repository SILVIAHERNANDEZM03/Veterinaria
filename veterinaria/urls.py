from django.contrib import admin
from rest_framework import routers
from django.urls import path
from vet.views import ListPersona, ListClientesFamilia, ListRelacionPersonasClientes, ListVacunas, \
    ListPacientesMascotas, ListPesos

router = routers.DefaultRouter()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Persona', ListPersona.as_view()),
    path('ClientesFamilia', ListClientesFamilia.as_view()),
    path('RelacionPersonasClientes', ListRelacionPersonasClientes.as_view()),
    path('PacientesMascotas', ListPacientesMascotas.as_view()),
    path('Vacunas', ListVacunas.as_view()),
    path('Pesos', ListPesos.as_view()),
]


