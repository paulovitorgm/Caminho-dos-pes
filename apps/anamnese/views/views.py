from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from apps.anamnese.forms import AnamneseForm
from apps.anamnese.models import AnamneseModel


class AnamneseListView(ListView):
    model = AnamneseModel
    template_name = 'anamnese/lista_de_anamneses.html'
    context_object_name = 'lista'


class AnamneseCreate(CreateView):
    model = AnamneseModel
    fields = '__all__'
    template_name = 'anamnese/form_anamnese.html'
    success_url = reverse_lazy('anamnese:listar')


class AnamneseUpdate(UpdateView):
    model = AnamneseModel
    form_class = AnamneseForm
    template_name = 'anamnese/form_anamnese.html'
    success_url = reverse_lazy('anamnese:listar')


class AnamneseDetail(DetailView):
    model = AnamneseModel
    template_name = 'anamnese/detalhes_anamnese.html'
    context_object_name = 'lista'


class AnamneseDelete(DeleteView):
    model = AnamneseModel
    context_object_name = 'lista'
    template_name = 'anamnese/deletar_anamnese.html'
    success_url = reverse_lazy('anamnese:listar')
