from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from rest_framework.viewsets import ModelViewSet

from apps.vendas.models import VendasModel
from apps.vendas.serializers import VendasSerializer


class VendasCreate(CreateView):
    model = VendasModel
    fields = '__all__'
    template_name = 'vendas/form_venda.html'
    success_url = reverse_lazy('vendas:listar')


class VendasList(ListView):
    model = VendasModel
    template_name = 'vendas/lista_de_vendas.html'
    context_object_name = 'lista'


class VendasDetail(DetailView):
    model = VendasModel
    template_name = 'vendas/detalhes_venda.html'
    context_object_name = 'lista'


class VendasUpdate(UpdateView):
    model = VendasModel
    fields = '__all__'
    template_name = 'vendas/form_venda.html'
    success_url = reverse_lazy('vendas:listar')


class VendasDelete(DeleteView):
    model = VendasModel
    context_object_name = 'lista'
    template_name = 'vendas/deletar_venda.html'
    success_url = reverse_lazy('vendas:listar')


class VendasViewset(ModelViewSet):
    queryset = VendasModel.objects.all()
    serializer_class = VendasSerializer
