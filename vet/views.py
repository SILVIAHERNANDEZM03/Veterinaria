from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from vet.serializers import Persona, ClientesFamilia, RelacionPersonasClientes, PacientesMascotas, Vacunas, Pesos


class Persona(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = Persona
    permission_classes = [permissions.IsAuthenticated]


class ClientesFamilia(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = ClientesFamilia
    permission_classes = [permissions.IsAuthenticated]


class RelacionPersonasClientes(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = RelacionPersonasClientes
    permission_classes = [permissions.IsAuthenticated]


class PacientesMascotas(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = PacientesMascotas
    permission_classes = [permissions.IsAuthenticated]


class Vacunas(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = Vacunas
    permission_classes = [permissions.IsAuthenticated]


class Pesos(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = Pesos
    permission_classes = [permissions.IsAuthenticated]