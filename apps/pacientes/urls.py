from django.urls import path

from apps.pacientes.views import (PacientesListView,
                                  PacientesCreate, PacientesDetail,
                                  PacientesUpdate, PacientesDelete)

app_name = 'pacientes'

urlpatterns = [
    path('', PacientesListView.as_view(), name='lista'),
    path('cadastrar/', PacientesCreate.as_view(), name='criar'),
    path('detalhar/<pk>/', PacientesDetail.as_view(), name='detalhar'),
    path('editar/<pk>/', PacientesUpdate.as_view(), name='editar'),
    path('deletar/<pk>/', PacientesDelete.as_view(), name='deletar'),

]
