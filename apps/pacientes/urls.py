from django.urls import path

from apps.pacientes.views import PacientesListView

app_name = 'pacientes'

urlpatterns = [
    path('', PacientesListView.as_view(), name='lista'),
]
