from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from vet.views import ListPersona, ListClientesFamilia, ListRelacionPersonasClientes, ListVacunas, \
    ListPacientesMascotas, ListPesos

router = routers.DefaultRouter()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('vet/', include('vet.urls'))

]


