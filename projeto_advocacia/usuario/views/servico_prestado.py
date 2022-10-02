from django.urls import reverse_lazy
from projeto_advocacia.core.views import CustomListView, CustomDetailView, CustomCreateView, CustomUpdateView, \
    CustomDeleteView
from projeto_advocacia.processo.models import PrestacaoServico
from projeto_advocacia.usuario.forms import PrestacaoServicoForm


class PrestacaoServicoList(CustomListView):
    model = PrestacaoServico
    queryset = PrestacaoServico.objects.all()
    paginate_by = 10
    ordering = ['pk']
    template_name = 'prestacao_servico/list.html'
    raiz = "Prestação de Serviços"
    titulo = "Lista de Prestação de Serviços"
    fields = '__all__'

    def campos_tabela(self):
        fields = []
        all_fields = self.model._meta.get_fields()
        if self.fields == '__all__':
            return all_fields
        for field in all_fields:
            if field.name in self.fields:
                fields.append(field)
        return fields

    def get_queryset(self):
        queryset = super(PrestacaoServicoList, self).get_queryset()
        if self.request.GET:
            filters = {}
            for index, valor in self.request.GET.items():
                if not valor:
                    continue
                if index == "csrfmiddlewaretoken":
                    continue
                filters[index] = valor
            try:
                queryset = queryset.filter(**filters)
            except:
                return []
        return queryset


class PrestacaoServicoDetail(CustomDetailView):
    model = PrestacaoServico
    template_name = 'prestacao_servico/detail.html'
    raiz = "Prestação de Serviços"
    titulo = "Detalhe da Prestação de Serviço"
    campos_tabela = model._meta.get_fields()


class PrestacaoServicoCreate(CustomCreateView):
    model = PrestacaoServico
    template_name = 'prestacao_servico/create.html'
    form_class = PrestacaoServicoForm
    success_url = reverse_lazy("prestacao_servicos_list")
    raiz = "Prestação de Serviços"
    titulo = "Adicionar nova Prestação de Serviço"


class PrestacaoServicoUpdate(CustomUpdateView):
    model = PrestacaoServico
    template_name = 'prestacao_servico/update.html'
    form_class = PrestacaoServicoForm
    raiz = "Prestação de Serviços"
    titulo = "Editar Prestação de Serviço"
    campos_filtro = ['autor', 'reu', 'juiz', 'advogado_autor', 'advogado_reu']

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        response = form_class(**self.get_form_kwargs())
        for field in response:
            if field.name in self.campos_filtro:
                field.initial = getattr(self.object, field.name)
        return response


class PrestacaoServicoDelete(CustomDeleteView):
    model = PrestacaoServico
    template_name = 'prestacao_servico/delete.html'
    success_url = reverse_lazy("prestacao_servicos_list")
    raiz = "Prestação de Serviços"
    titulo = "Deletar Prestação de Serviço"
    descricao = "Prestação de Serviço"
    campos_tabela = model._meta.get_fields()
