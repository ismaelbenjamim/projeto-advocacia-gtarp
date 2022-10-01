from django.urls import path, include
from projeto_advocacia.usuario.views import UsuarioList, UsuarioCreate, UsuarioUpdate, UsuarioDelete, UsuarioDetail, \
    ClienteList, ClienteCreate, ClienteUpdate, ClienteDelete, ClienteDetail

urlpatterns = [
    path('listar/', UsuarioList.as_view(), name='usuarios_list'),
    path('adicionar/', UsuarioCreate.as_view(), name='usuarios_create'),
    path('editar/<str:pk>/', UsuarioUpdate.as_view(), name='usuarios_update'),
    path('deletar/<str:pk>/', UsuarioDelete.as_view(), name='usuarios_delete'),
    path('visualizar/<str:pk>/', UsuarioDetail.as_view(), name='usuarios_detail'),

    path('clientes/listar/', ClienteList.as_view(), name='clientes_list'),
    path('clientes/adicionar/', ClienteCreate.as_view(), name='clientes_create'),
    path('clientes/editar/<str:pk>/', ClienteUpdate.as_view(), name='clientes_update'),
    path('clientes/deletar/<str:pk>/', ClienteDelete.as_view(), name='clientes_delete'),
    path('clientes/visualizar/<str:pk>/', ClienteDetail.as_view(), name='clientes_detail'),
]