from django.contrib.auth.views import LogoutView
from django.urls import path

from apps.autenticacao.views import (
    UserCreate,
    UserDelete,
    UserDetail,
    UserLogin,
    UserUpdate,
    UserView,
)

app_name = 'autenticacao'

urlpatterns = [
    path('', UserView.as_view(), name='listar'),
    path('detalhar/<int:pk>/', UserDetail.as_view(), name='detalhar'),
    path('deletar/<int:pk>/', UserDelete.as_view(), name='deletar'),
    path('editar/<int:pk>/', UserUpdate.as_view(), name='editar'),
    path('criar/', UserCreate.as_view(), name='criar'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
