from django.urls import reverse_lazy

from projeto_advocacia.core.views import CustomListView, CustomDetailView, CustomCreateView, CustomUpdateView, \
    CustomDeleteView
from projeto_advocacia.processo.forms import ProcessoForm, LeiForm
from projeto_advocacia.processo.models import Processo, Lei


class ProcessoList(CustomListView):
    model = Processo
    queryset = Processo.objects.all()
    paginate_by = 10
    ordering = ['pk']
    template_name = 'processo/list.html'
    raiz = "Processos"
    titulo = "Lista de Processos"
    campos_tabela = ['Número de processo', 'Autor', 'Réu', 'Juiz', 'Advogado do Autor']

    def get_queryset(self):
        queryset = super(ProcessoList, self).get_queryset()
        if self.request.GET:
            filters = {}
            for index, valor in self.request.GET.items():
                if not valor:
                    continue
                if index == "csrfmiddlewaretoken":
                    continue
                if index in ['autor', 'reu', 'juiz', 'advogado_autor', 'advogado_reu']:
                    index = f'{index}__identidade'
                filters[index] = valor
            try:
                queryset = queryset.filter(**filters)
            except:
                return []
        return queryset


class ProcessoDetail(CustomDetailView):
    model = Processo
    template_name = 'processo/detail.html'
    raiz = "Processos"
    titulo = "Detalhe do Processo"
    campos_tabela = model._meta.get_fields()
    campos_filtro = ['descricao', 'postulatoria', 'instrutoria', 'decisoria', 'recursal', 'executiva']


class ProcessoCreate(CustomCreateView):
    model = Processo
    template_name = 'processo/create.html'
    form_class = ProcessoForm
    success_url = reverse_lazy("processos_list")
    raiz = "Processos"
    titulo = "Adicionar novo processo"


class ProcessoUpdate(CustomUpdateView):
    model = Processo
    template_name = 'processo/update.html'
    form_class = ProcessoForm
    success_url = reverse_lazy("processos_list")
    raiz = "Processos"
    titulo = "Editar Processo"
    campos_filtro = ['autor', 'reu', 'juiz', 'advogado_autor', 'advogado_reu']

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        response = form_class(**self.get_form_kwargs())
        for field in response:
            if field.name in self.campos_filtro:
                field.initial = getattr(self.object, field.name)
        return response

    def get_success_url(self):
        self.success_url = reverse_lazy("processos_detail", kwargs={"pk": self.object.pk})
        return super().get_success_url()


class ProcessoDelete(CustomDeleteView):
    model = Processo
    template_name = 'processo/delete.html'
    success_url = reverse_lazy("processos_list")
    raiz = "Processos"
    titulo = "Deletar Processo"
    descricao = "Processo"
    campos_tabela = model._meta.get_fields()


class LeiList(CustomListView):
    model = Lei
    queryset = Lei.objects.all()
    paginate_by = 10
    ordering = ['pk']
    template_name = 'legislacao/list.html'
    raiz = "Leis"
    titulo = "Lista de Leis"
    campos_tabela = ['Categoria', 'Artigo', 'Descrição', 'Pena base', 'Fiança', 'Agravante']

    def get_queryset(self):
        queryset = super(LeiList, self).get_queryset()
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


class LeiDetail(CustomDetailView):
    model = Lei
    template_name = 'legislacao/detail.html'
    raiz = "Leis"
    titulo = "Detalhe do Lei"
    campos_tabela = model._meta.get_fields()


class LeiCreate(CustomCreateView):
    model = Lei
    template_name = 'legislacao/create.html'
    form_class = LeiForm
    success_url = reverse_lazy("leis_list")
    raiz = "Leis"
    titulo = "Adicionar nova lei"


class LeiUpdate(CustomUpdateView):
    model = Lei
    template_name = 'legislacao/update.html'
    form_class = LeiForm
    raiz = "Leis"
    titulo = "Editar Lei"
    campos_filtro = ['autor', 'reu', 'juiz', 'advogado_autor', 'advogado_reu']

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        response = form_class(**self.get_form_kwargs())
        for field in response:
            if field.name in self.campos_filtro:
                field.initial = getattr(self.object, field.name)
        return response


class LeiDelete(CustomDeleteView):
    model = Lei
    template_name = 'legislacao/delete.html'
    success_url = reverse_lazy("leis_list")
    raiz = "Leis"
    titulo = "Deletar Lei"
    descricao = "Lei"
    campos_tabela = model._meta.get_fields()
