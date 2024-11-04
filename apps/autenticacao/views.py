from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from apps.autenticacao.forms.criar_user_form import UserForm
from apps.autenticacao.forms.editar_user_form import EditarUserForm


class UserView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'autenticacao/lista_autenticacao.html'
    context_object_name = 'lista'


class UserCreate(CreateView):
    model = User
    form_class = UserForm
    template_name = 'autenticacao/form_autenticacao.html'
    success_url = reverse_lazy('autenticacao:login')


class UserDetail(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'autenticacao/detalhes_usuario.html'
    context_object_name = 'lista'
    permission_required = 'detail_user'


class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    form_class = EditarUserForm
    template_name = 'autenticacao/form_autenticacao.html'

    def get_success_url(self):
        return reverse_lazy('autenticacao:detalhar', kwargs={'pk': self.object.pk})


class UserDelete(LoginRequiredMixin, DeleteView):
    model = User
    context_object_name = 'lista'
    template_name = 'autenticacao/deletar_usuario.html'
    success_url = reverse_lazy('autenticacao:criar')


class UserLogin(LoginView):
    template_name = 'autenticacao/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy(
            'autenticacao:detalhar', kwargs={'pk': self.request.user.id}
        )
