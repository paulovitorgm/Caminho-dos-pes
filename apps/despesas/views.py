from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from rest_framework.viewsets import ModelViewSet

from apps.despesas.models import DespesasModel
from apps.despesas.serializers import DespesasSerializer


class DespesasCreate(CreateView):
    model = DespesasModel
    fields = '__all__'
    template_name = 'despesas/form_despesa.html'
    success_url = reverse_lazy('despesas:listar')


class DespesasList(ListView):
    model = DespesasModel
    template_name = 'despesas/lista_de_despesas.html'
    context_object_name = 'lista'


class DespesasDetail(DetailView):
    model = DespesasModel
    template_name = 'despesas/detalhes_despesa.html'
    context_object_name = 'lista'


class DespesasUpdate(UpdateView):
    model = DespesasModel
    fields = '__all__'
    template_name = 'despesas/form_despesa.html'
    success_url = reverse_lazy('despesas:listar')


class DespesasDelete(DeleteView):
    model = DespesasModel
    context_object_name = 'lista'
    template_name = 'despesas/deletar_despesa.html'
    success_url = reverse_lazy('despesas:listar')


class DespesasViewset(ModelViewSet):
    queryset = DespesasModel.objects.all()
    serializer_class = DespesasSerializer
