from django.urls import path

from apps.anamnese.views import (
    AnamneseCreate,
    AnamneseDelete,
    AnamneseDetail,
    AnamneseListView,
    AnamneseUpdate,
)

app_name = 'anamnese'

urlpatterns = [
    path('', AnamneseListView.as_view(), name='listar'),
    path('criar/', AnamneseCreate.as_view(), name='criar'),
    path('detalhar/<pk>/', AnamneseDetail.as_view(), name='detalhar'),
    path('deletar/<pk>/', AnamneseDelete.as_view(), name='deletar'),
    path('editar/<pk>/', AnamneseUpdate.as_view(), name='editar'),
]
