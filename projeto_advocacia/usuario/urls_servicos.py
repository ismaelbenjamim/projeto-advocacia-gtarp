from django.urls import path, include

from projeto_advocacia.usuario.views import ServicoList, ServicoCreate, ServicoUpdate, ServicoDelete, ServicoDetail, \
    PrestacaoServicoList, PrestacaoServicoCreate, PrestacaoServicoUpdate, PrestacaoServicoDelete, PrestacaoServicoDetail

urlpatterns = [
    path('listar/', ServicoList.as_view(), name='servicos_list'),
    path('adicionar/', ServicoCreate.as_view(), name='servicos_create'),
    path('editar/<str:pk>/', ServicoUpdate.as_view(), name='servicos_update'),
    path('deletar/<str:pk>/', ServicoDelete.as_view(), name='servicos_delete'),
    path('visualizar/<str:pk>/', ServicoDetail.as_view(), name='servicos_detail'),

    path('prestacao-servico/listar/', PrestacaoServicoList.as_view(), name='prestacao_servicos_list'),
    path('prestacao-servico/adicionar/', PrestacaoServicoCreate.as_view(), name='prestacao_servicos_create'),
    path('prestacao-servico/editar/<str:pk>/', PrestacaoServicoUpdate.as_view(), name='prestacao_servicos_update'),
    path('prestacao-servico/deletar/<str:pk>/', PrestacaoServicoDelete.as_view(), name='prestacao_servicos_delete'),
    path('prestacao-servico/visualizar/<str:pk>/', PrestacaoServicoDetail.as_view(), name='prestacao_servicos_detail'),
]
