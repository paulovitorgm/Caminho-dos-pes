from django.urls import path

from apps.despesas.views import (
    DespesasCreate,
    DespesasDelete,
    DespesasDetail,
    DespesasList,
    DespesasUpdate,
)

app_name = 'despesas'

urlpatterns = [
    path('', DespesasList.as_view(), name='listar'),
    path('detalhes/<pk>/', DespesasDetail.as_view(), name='detalhar'),
    path('deletar/<pk>/', DespesasDelete.as_view(), name='deletar'),
    path('editar/<pk>/', DespesasUpdate.as_view(), name='editar'),
    path('criar/', DespesasCreate.as_view(), name='criar'),
]
