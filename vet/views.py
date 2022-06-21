from rest_framework import generics
from vet import models
from .serializers import PersonaSerializer, ClientesFamiliaSerializer, RelacionPersonasClientesSerializer, PacientesMascotasSerializer, VacunasSerializer, PesosSerializer


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


class DetailPacientesMascotas(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PacientesMascotas.objects.all()
    serializer_class = PacientesMascotasSerializer


class ListVacunas(generics.ListCreateAPIView):
    queryset = models.Vacunas.objects.all()
    serializer_class = VacunasSerializer


class DetailVacunas(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Vacunas.objects.all()
    serializer_class = VacunasSerializer


class ListPesos(generics.ListCreateAPIView):
    queryset = models.Pesos.objects.all()
    serializer_class = PesosSerializer


class DetailPesos(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Pesos.objects.all()
    serializer_class = PesosSerializer

