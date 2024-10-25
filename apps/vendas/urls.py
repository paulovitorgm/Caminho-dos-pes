from django.urls import path

from apps.vendas.views import (
    VendasCreate,
    VendasDelete,
    VendasDetail,
    VendasList,
    VendasUpdate,
)

app_name = 'vendas'

urlpatterns = [
    path('', VendasList.as_view(), name='listar'),
    path('detalhes/<pk>/', VendasDetail.as_view(), name='detalhar'),
    path('deletar/<pk>/', VendasDelete.as_view(), name='deletar'),
    path('editar/<pk>/', VendasUpdate.as_view(), name='editar'),
    path('criar/', VendasCreate.as_view(), name='criar'),
]
