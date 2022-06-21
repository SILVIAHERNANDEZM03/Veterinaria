from django.contrib import admin
from rest_framework import routers
from django.urls import path
from vet.views import ListPersona, ListClientesFamilia, ListRelacionPersonasClientes, ListVacunas, \
    ListPacientesMascotas, ListPesos, DetailPacientesMascotas, DetailVacunas, DetailPesos

router = routers.DefaultRouter()
urlpatterns = [

    path('Persona', ListPersona.as_view()),
    path('ClientesFamilia', ListClientesFamilia.as_view()),
    path('RelacionPersonasClientes', ListRelacionPersonasClientes.as_view()),
    path('PacientesMascotas', ListPacientesMascotas.as_view()),
    path('PacientesMascotas/<int:pk>/', DetailPacientesMascotas.as_view()),
    path('Vacunas', ListVacunas.as_view()),
    path('Vacunas/<int:pk>/', DetailVacunas.as_view()),
    path('Pesos', ListPesos.as_view()),
    path('Pesos/<int:pk>/', DetailPesos.as_view()),
]
