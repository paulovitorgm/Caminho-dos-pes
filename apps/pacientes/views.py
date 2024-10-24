from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from apps.pacientes.models.pacientes import PacientesModel


class PacientesListView(ListView):
    model = PacientesModel
    template_name = 'pacientes/lista_de_pacientes.html'
    context_object_name = 'lista'


class PacientesCreate(CreateView):
    model = PacientesModel
    template_name = 'form.html'
    fields = '__all__'
    success_url = reverse_lazy('pacientes:lista')


class PacientesDetail(DetailView):
    model = PacientesModel
    template_name = 'pacientes/detalhes_paciente.html'
    context_object_name = 'lista'


class PacientesUpdate(UpdateView):
    model = PacientesModel
    template_name = 'form.html'
    fields = '__all__'
    success_url = reverse_lazy('pacientes:lista')


class PacientesDelete(DeleteView):
    model = PacientesModel
    template_name = 'pacientes/deletar_paciente.html'
    success_url = reverse_lazy('pacientes:lista')
    context_object_name = 'lista'
