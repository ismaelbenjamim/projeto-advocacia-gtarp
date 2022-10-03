from django import forms
from projeto_advocacia.core.forms import CustomModelForm
from projeto_advocacia.core.views import CustomListView, CustomDetailView, CustomCreateView, CustomUpdateView, \
    CustomDeleteView
from projeto_advocacia.usuario.models import Servico


class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.field.__class__.__name__ == "BooleanField":
                visible.field.widget.attrs['class'] = 'form-check-input mb-2'
            else:
                visible.field.widget.attrs['class'] = 'form-control mb-2'


class ServicoList(CustomListView):
    class FiltersForm(CustomModelForm):
        class Meta:
            model = Servico
            fields = ['descricao', 'valor_base', 'cargo_responsavel', 'is_ativo']

    model = Servico
    queryset = Servico.objects.all()
    paginate_by = 10
    ordering = ['pk']
    template_name = 'servico/list.html'
    raiz = "Serviços"
    titulo = "Lista de Serviços"
    url_prefix = "servicos"
    fields = ['id', 'descricao', 'valor_base', 'cargo_responsavel', 'is_ativo']
    filters_form = FiltersForm


class ServicoDetail(CustomDetailView):
    class DetailForm(ServicoForm):
        class Meta:
            model = Servico
            fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['disabled'] = True


    model = Servico
    template_name = 'servico/detail.html'
    raiz = "Serviços"
    titulo = "Detalhe de Serviços"
    url_prefix = "servicos"
    form_class = DetailForm


class ServicoCreate(CustomCreateView):
    class CreateForm(ServicoForm):
        class Meta:
            model = Servico
            fields = '__all__'

    model = Servico
    template_name = 'servico/create.html'
    form_class = CreateForm
    raiz = "Serviços"
    titulo = "Adicionar novos Serviços"
    url_prefix = "servicos"


class ServicoUpdate(CustomUpdateView):
    class UpdateForm(ServicoForm):
        class Meta:
            model = Servico
            fields = '__all__'

    model = Servico
    template_name = 'servico/update.html'
    form_class = UpdateForm
    raiz = "Serviços"
    titulo = "Editar Serviços"
    url_prefix = "servicos"


class ServicoDelete(CustomDeleteView):
    class DeleteForm(ServicoForm):
        class Meta:
            model = Servico
            fields = '__all__'

    model = Servico
    template_name = 'servico/delete.html'
    raiz = "Serviços"
    titulo = "Deletar Serviços"
    descricao = "Serviços"
    url_prefix = "servicos"
    form_class = DeleteForm

