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
    path('detalhar/<int:pk>/', AnamneseDetail.as_view(), name='detalhar'),
    path('deletar/<int:pk>/', AnamneseDelete.as_view(), name='deletar'),
    path('editar/<int:pk>/', AnamneseUpdate.as_view(), name='editar'),
]
