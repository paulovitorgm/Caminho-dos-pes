from django.shortcuts import render
from django.views.generic.list import ListView

from apps.pacientes.models import PacientesModel


class PacientesListView(ListView):
    model = PacientesModel
    template_name = 'index.html'

