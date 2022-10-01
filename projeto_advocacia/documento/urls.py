from django.urls import path, include

from projeto_advocacia.documento.views import DocumentoDetail, DocumentoDelete, DocumentoUpdate, DocumentoCreate, DocumentoList

urlpatterns = [
    path('listar/', DocumentoList.as_view(), name='documentos_list'),
    path('adicionar/', DocumentoCreate.as_view(), name='documentos_create'),
    path('editar/<str:pk>/', DocumentoUpdate.as_view(), name='documentos_update'),
    path('deletar/<str:pk>/', DocumentoDelete.as_view(), name='documentos_delete'),
    path('visualizar/<str:pk>/', DocumentoDetail.as_view(), name='documentos_detail'),
]
