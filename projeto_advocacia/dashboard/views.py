from django.shortcuts import render
from django.views.generic import TemplateView

from projeto_advocacia.processo.models import Processo


class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['processos'] = Processo.objects.all().order_by('-data_abertura')[:4]
        return context
