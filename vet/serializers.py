from rest_framework import serializers
from vet import models


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'nombrepersona',
            'apellidopersona',
            'telefono',
            'direccion',
            'email'
        )
        model=models.Persona


class ClientesFamiliaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'PrimerApellido',
            'CuentaBanco',
            'telefono'
        )
        model=models.ClientesFamilia


class RelacionPersonasClientesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'IDClientesFamilia',
            'IDPersona'
        )
        model=models.RelacionPersonasClientes


class PacientesMascotasSerializer(serializers.ModelSerializer):
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
        model=models.PacientesMascotas


class VacunasSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'IDPacientesMascotas',
            'Fecha',
            'Enfermedad',
            'FechaProxima'

        )
        model = models.Vacunas


class PesosSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'IDPacientesMascotas',
            'FechaConsulta',
            'Peso'
        )
        model = models.Pesos

