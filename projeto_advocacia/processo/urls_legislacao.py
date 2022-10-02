from django.urls import path, include

from projeto_advocacia.processo.views import LeiDetail, LeiDelete, LeiUpdate, LeiCreate, LeiList

urlpatterns = [
    path('listar/', LeiList.as_view(), name='leis_list'),
    path('adicionar/', LeiCreate.as_view(), name='leis_create'),
    path('editar/<str:pk>/', LeiUpdate.as_view(), name='leis_update'),
    path('deletar/<str:pk>/', LeiDelete.as_view(), name='leis_delete'),
    path('visualizar/<str:pk>/', LeiDetail.as_view(), name='leis_detail'),
]
