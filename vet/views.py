from django.shortcuts import render
from rest_framework import generics, viewsets

from vet import models
from .serializers import PersonaSerializer,ClientesFamiliaSerializer, RelacionPersonasClientesSerializer,PacientesMascotasSerializer, VacunasSerializer, PesosSerializer


class ListPersona(generics.ListCreateAPIView):
    queryset = models.Persona.objects.all()
    serializer_class = PersonaSerializer


class ListClientesFamilia(generics.ListCreateAPIView):
    queryset = models.ClientesFamilia.objects.all()
    serializer_class = ClientesFamiliaSerializer


class ListRelacionPersonasClientes(generics.ListCreateAPIView):
    queryset = models.RelacionPersonasClientes.objects.all()
    serializer_class = RelacionPersonasClientesSerializer


class ListPacientesMascotas(generics.ListCreateAPIView):
    queryset = models.PacientesMascotas.objects.all()
    serializer_class = PacientesMascotasSerializer


class ListVacunas(generics.ListCreateAPIView):
    queryset = models.Vacunas.objects.all()
    serializer_class = VacunasSerializer


class ListPesos(generics.ListCreateAPIView):
    queryset = models.Pesos.objects.all()
    serializer_class = PesosSerializer

