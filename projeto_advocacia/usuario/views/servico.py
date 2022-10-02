from django import forms
from django.urls import reverse_lazy

from projeto_advocacia.core.views_base import CustomListView, CustomDetailView, CustomCreateView, CustomUpdateView, \
    CustomDeleteView
from projeto_advocacia.usuario.forms import ServicoForm
from projeto_advocacia.usuario.models import Servico


class ServicoFilters(forms.Form):
    descricao = forms.CharField(label='Descrição', required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Descrição'}))
    valor_base = forms.CharField(label='Valor Base', required=False,
                                 widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Valor Base'}))
    cargo_responsavel = forms.CharField(label='Cargo responsável', required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Cargo responsável'}))
    is_ativo = forms.BooleanField(label='É um serviço ativo?', required=False,
                              widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))


class ServicoList(CustomListView):
    model = Servico
    queryset = Servico.objects.all()
    paginate_by = 10
    ordering = ['pk']
    template_name = 'servico/list.html'
    raiz = "Serviços"
    titulo = "Lista de Serviços"
    url_prefix = "servicos"
    fields = ['id', 'descricao', 'valor_base', 'cargo_responsavel', 'is_ativo']
    filters_form = ServicoFilters

    def get_queryset(self):
        queryset = super(ServicoList, self).get_queryset()
        if self.request.GET:
            filters = {}
            for index, valor in self.request.GET.items():
                if valor == 'on':
                    valor = True
                if valor and index in list(self.filters_form().fields):
                    filters[index] = valor
            try:
                queryset = queryset.filter(**filters)
            except:
                return []
        return queryset


class ServicoDetail(CustomDetailView):
    model = Servico
    template_name = 'servico/detail.html'
    raiz = "Serviços"
    titulo = "Detalhe do Serviço"
    url_prefix = "servicos"
    fields = ['id', 'descricao', 'valor_base', 'cargo_responsavel', 'is_ativo']


class ServicoCreate(CustomCreateView):
    model = Servico
    template_name = 'servico/create.html'
    form_class = ServicoForm
    raiz = "Serviços"
    titulo = "Adicionar novo Serviço"
    url_prefix = "servicos"


class ServicoUpdate(CustomUpdateView):
    model = Servico
    template_name = 'servico/update.html'
    form_class = ServicoForm
    raiz = "Serviços"
    titulo = "Editar Serviço"
    url_prefix = "servicos"
    campos_filtro = '__all__'

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        response = form_class(**self.get_form_kwargs())
        for field in response:
            if field.name in self.campos_filtro:
                field.initial = getattr(self.object, field.name)
        return response


class ServicoDelete(CustomDeleteView):
    model = Servico
    template_name = 'servico/delete.html'
    raiz = "Serviços"
    titulo = "Deletar Serviço"
    descricao = "Serviço"
    url_prefix = "servicos"
    fields = '__all__'

