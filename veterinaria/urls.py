from django.urls import include, path
from django.contrib.auth import admin
from rest_framework import routers
from vet import views
from vet.views import Persona

router = routers.DefaultRouter()
router.register(r'Persona', views.Persona)
router.register(r'ClientesFamilia', views.ClientesFamilia)
router.register(r'RelacionPersonasClientes', views.RelacionPersonasClientes)
router.register(r'PacientesMascotas', views.PacientesMascotas)
router.register(r'Vacunas', views.Vacunas)
router.register(r'Pesos', views.Pesos)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('Persona', views.Persona),

]

