import datetime

from django.shortcuts import render
from django.views.generic import TemplateView

from projeto_advocacia.processo.models import Processo
from projeto_advocacia.usuario.models import Usuario


class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_porcentagem(self, val1, val2):
        if val1 != 0:
            valor = (val2 * 100)/val1
        else:
            valor = 0.0
        return valor

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['processos'] = Processo.objects.all().order_by('-data_abertura')[:4]
        mes_atual = datetime.datetime.now().month
        mes_passado = datetime.datetime.now().month - 1

        p_aberto_mes_atual = Processo.objects.filter(data_abertura__month=mes_atual)
        p_aberto_mes_passd = Processo.objects.filter(data_abertura__month=mes_passado)

        p_encerrado_mes_atual = p_aberto_mes_atual.filter(fase="Executiva")
        p_encerrado_mes_passd = p_aberto_mes_passd.filter(fase="Executiva")

        adv_mes_atual = Usuario.objects.filter(date_joined__month=mes_atual, organizacao='2')
        adv_mes_passd = Usuario.objects.filter(date_joined__month=mes_passado, organizacao='2')

        context['info'] = {
            "processos_abertos": [
                len(p_aberto_mes_atual),
                len(p_aberto_mes_passd),
                self.get_porcentagem(len(p_aberto_mes_passd), len(p_aberto_mes_atual))
            ],
            "processos_encerrados": [
                len(p_encerrado_mes_atual),
                len(p_encerrado_mes_passd),
                self.get_porcentagem(len(p_encerrado_mes_passd), len(p_encerrado_mes_atual))
            ],
            "advogados_disponiveis": [
                len(adv_mes_atual),
                len(adv_mes_passd),
                self.get_porcentagem(len(adv_mes_passd), len(adv_mes_atual))
            ],
            "tipo_processo": {
                "conhecimento": len(Processo.objects.filter(tipo="Conhecimento")),
                "cautelar": len(Processo.objects.filter(tipo="Cautelar")),
                "execucao": len(Processo.objects.filter(tipo="Execução")),
                "total": len(Processo.objects.all()),
            }
        }
        return context
