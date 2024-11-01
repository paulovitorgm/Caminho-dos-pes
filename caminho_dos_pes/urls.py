from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from apps.anamnese.views.api import AnamnesesViewset
from apps.despesas.views.api import DespesasViewset
from apps.pacientes.views.api import PacientesViewset
from apps.vendas.views.api import VendasViewset

router = routers.DefaultRouter()

router.register('pacientes', PacientesViewset, basename='pacientes')
router.register('anamnese', AnamnesesViewset, basename='anamneses')
router.register('vendas', VendasViewset)
router.register('despesas', DespesasViewset)

app_name = 'api'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pacientes/', include('apps.pacientes.urls')),
    path('anamnese/', include('apps.anamnese.urls')),
    path('vendas/', include('apps.vendas.urls')),
    path('despesas/', include('apps.despesas.urls')),
    path('api/', include((router.urls, 'api'))),
]
