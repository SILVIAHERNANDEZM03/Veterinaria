from rest_framework import serializers
from vet import models


class Persona(serializers.ModelSerializer):
    class Meta:
        fields = (
            'nombrepersona',
            'apellidopersona',
            'telefono',
            'direccion',
            'email'
        )
        model=models.Persona


class ClientesFamilia(serializers.ModelSerializer):
    class Meta:
        fields = (
            'PrimerApellido',
            'CuentaBanco',
            'telefono'
        )
        model=models.ClientesFamilia


class RelacionPersonasClientes(serializers.ModelSerializer):
    class Meta:
        fields = (
            'IDClientesFamilia',
            'IDPersona'
        )
        model=models.RelacionPersonasClientes


class PacientesMascotas(serializers.ModelSerializer):
    class Meta:
        fields = (
            'IDClientesFamilia',
            'AliasMascota',
            'Especie',
            'Raza',
            'ColorPelo',
            'FechaNacimiento',
            'Vacunaciones'

        )
        model=models.RelacionPersonasClientes


class Vacunas(serializers.ModelSerializer):
    class Meta:
        fields = (
            'IDPacientesMascotas',
            'Fecha',
            'Enfermedad',
            'FechaProxima'

        )
        model = models.Vacunas


class Pesos(serializers.ModelSerializer):
    class Meta:
        fields = (
            'IDPacientesMascotas',
            'FechaConsulta',
            'Peso'
        )
        model = models.Pesos

