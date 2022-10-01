from django.urls import path, include

from projeto_advocacia.dashboard.views import DashboardView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('usuarios/', include('projeto_advocacia.usuario.urls')),
    path('servicos/', include('projeto_advocacia.usuario.urls_servicos')),
    path('processos/', include('projeto_advocacia.processo.urls_processo')),
    path('legislacao/', include('projeto_advocacia.processo.urls_legislacao')),
    path('documentos/', include('projeto_advocacia.documento.urls')),
]
