from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from rest_framework.viewsets import ModelViewSet

from apps.pacientes.models import PacientesModel
from apps.pacientes.serializers import PacientesSerializer


class PacientesListView(ListView):
    model = PacientesModel
    template_name = 'pacientes/lista_de_pacientes.html'
    context_object_name = 'lista'


class PacientesCreate(CreateView):
    model = PacientesModel
    template_name = 'pacientes/form_paciente.html'
    fields = '__all__'
    success_url = reverse_lazy('pacientes:listar')


class PacientesDetail(DetailView):
    model = PacientesModel
    template_name = 'pacientes/detalhes_paciente.html'
    context_object_name = 'lista'


class PacientesUpdate(UpdateView):
    model = PacientesModel
    template_name = 'pacientes/form_paciente.html'
    fields = '__all__'
    success_url = reverse_lazy('pacientes:listar')


class PacientesDelete(DeleteView):
    model = PacientesModel
    template_name = 'pacientes/deletar_paciente.html'
    success_url = reverse_lazy('pacientes:listar')
    context_object_name = 'lista'


class PacientesViewset(ModelViewSet):
    queryset = PacientesModel.objects.all()
    serializer_class = PacientesSerializer
