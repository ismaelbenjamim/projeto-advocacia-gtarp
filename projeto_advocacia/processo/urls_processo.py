from django.urls import path, include

from projeto_advocacia.processo.views.processo import ProcessoList, ProcessoDetail, ProcessoCreate, ProcessoUpdate, \
    ProcessoDelete

urlpatterns = [
    path('listar/', ProcessoList.as_view(), name='processos_list'),
    path('adicionar/', ProcessoCreate.as_view(), name='processos_create'),
    path('editar/<str:pk>/', ProcessoUpdate.as_view(), name='processos_update'),
    path('deletar/<str:pk>/', ProcessoDelete.as_view(), name='processos_delete'),
    path('visualizar/<str:pk>/', ProcessoDetail.as_view(), name='processos_detail'),
]
