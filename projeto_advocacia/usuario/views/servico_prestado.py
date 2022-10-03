from django import forms
from projeto_advocacia.core.forms import CustomModelForm
from projeto_advocacia.core.views import CustomListView, CustomDetailView, CustomCreateView, CustomUpdateView, \
    CustomDeleteView
from projeto_advocacia.processo.models import PrestacaoServico


class PrestacaoServicoForm(forms.ModelForm):
    class Meta:
        model = PrestacaoServico
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.field.__class__.__name__ == "BooleanField":
                visible.field.widget.attrs['class'] = 'form-check-input mb-2'
            else:
                visible.field.widget.attrs['class'] = 'form-control mb-2'


class PrestacaoServicoList(CustomListView):
    class FiltersForm(CustomModelForm):
        class Meta:
            model = PrestacaoServico
            fields = ['responsavel', 'servico', 'descricao', 'valor', 'cliente']

    model = PrestacaoServico
    queryset = PrestacaoServico.objects.all()
    paginate_by = 10
    ordering = ['pk']
    template_name = 'prestacao_servico/list.html'
    raiz = "Prestação de Serviços"
    titulo = "Lista de Prestação de Serviços"
    url_prefix = "prestacao_servicos"
    fields = ['id', 'responsavel', 'servico', 'descricao', 'valor', 'cliente']
    filters_form = FiltersForm


class PrestacaoServicoDetail(CustomDetailView):
    class DetailForm(PrestacaoServicoForm):
        class Meta:
            model = PrestacaoServico
            fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['disabled'] = True


    model = PrestacaoServico
    template_name = 'prestacao_servico/detail.html'
    raiz = "Prestação de Serviços"
    titulo = "Detalhe da Prestação de Serviços"
    url_prefix = "prestacao_servicos"
    form_class = DetailForm


class PrestacaoServicoCreate(CustomCreateView):
    class CreateForm(PrestacaoServicoForm):
        class Meta:
            model = PrestacaoServico
            fields = '__all__'

    model = PrestacaoServico
    template_name = 'prestacao_servico/create.html'
    form_class = CreateForm
    raiz = "Prestação de Serviços"
    titulo = "Adicionar nova Prestação de Serviços"
    url_prefix = "prestacao_servicos"


class PrestacaoServicoUpdate(CustomUpdateView):
    class UpdateForm(PrestacaoServicoForm):
        class Meta:
            model = PrestacaoServico
            fields = '__all__'

    model = PrestacaoServico
    template_name = 'prestacao_servico/update.html'
    form_class = UpdateForm
    raiz = "Prestação de Serviços"
    titulo = "Editar Prestação de Serviços"
    url_prefix = "prestacao_servicos"


class PrestacaoServicoDelete(CustomDeleteView):
    class DeleteForm(PrestacaoServicoForm):
        class Meta:
            model = PrestacaoServico
            fields = '__all__'

    model = PrestacaoServico
    template_name = 'prestacao_servico/delete.html'
    raiz = "Prestação de Serviços"
    titulo = "Deletar Prestação de Serviços"
    descricao = "Prestação de Serviços"
    url_prefix = "prestacao_servicos"
    form_class = DeleteForm

