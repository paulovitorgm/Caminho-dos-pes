from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from apps.anamnese.views import AnamnesesViewset
from apps.despesas.views import DespesasViewset
from apps.pacientes.views import PacientesViewset
from apps.vendas.views import VendasViewset


router = routers.DefaultRouter()
router.register('pacientes', PacientesViewset)
router.register('anamnese', AnamnesesViewset)
router.register('vendas', VendasViewset)
router.register('despesas', DespesasViewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pacientes/', include('apps.pacientes.urls')),
    path('anamnese/', include('apps.anamnese.urls')),
    path('vendas/', include('apps.vendas.urls')),
    path('despesas/', include('apps.despesas.urls')),
    path('api/', include(router.urls))
]
