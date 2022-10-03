from django import forms
from projeto_advocacia.core.forms import CustomModelForm
from projeto_advocacia.core.views import CustomListView, CustomDetailView, CustomCreateView, CustomUpdateView, \
    CustomDeleteView
from projeto_advocacia.processo.models import Processo


class ProcessoForm(forms.ModelForm):
    class Meta:
        model = Processo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.field.__class__.__name__ == "BooleanField":
                visible.field.widget.attrs['class'] = 'form-check-input mb-2'
            else:
                visible.field.widget.attrs['class'] = 'form-control mb-2'


class ProcessoList(CustomListView):
    class FiltersForm(CustomModelForm):
        class Meta:
            model = Processo
            fields = ['numero_processo', 'autor', 'reu', 'juiz', 'advogado_autor', 'advogado_reu', 'data_abertura',
                      'fase', 'tipo']

    model = Processo
    queryset = Processo.objects.all()
    paginate_by = 10
    ordering = ['pk']
    template_name = 'processo/list.html'
    raiz = "Prestação de Serviços"
    titulo = "Lista de Prestação de Serviços"
    url_prefix = "processos"
    fields = ['numero_processo', 'autor', 'reu', 'juiz', 'advogado_autor', 'advogado_reu', 'data_abertura',
              'fase', 'tipo']
    filters_form = FiltersForm


class ProcessoDetail(CustomDetailView):
    class DetailForm(ProcessoForm):
        class Meta:
            model = Processo
            fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['disabled'] = True


    model = Processo
    template_name = 'processo/detail.html'
    raiz = "Prestação de Serviços"
    titulo = "Detalhe da Prestação de Serviços"
    url_prefix = "processos"
    form_class = DetailForm


class ProcessoCreate(CustomCreateView):
    class CreateForm(ProcessoForm):
        class Meta:
            model = Processo
            fields = '__all__'

    model = Processo
    template_name = 'processo/create.html'
    form_class = CreateForm
    raiz = "Prestação de Serviços"
    titulo = "Adicionar nova Prestação de Serviços"
    url_prefix = "processos"


class ProcessoUpdate(CustomUpdateView):
    class UpdateForm(ProcessoForm):
        class Meta:
            model = Processo
            fields = '__all__'

    model = Processo
    template_name = 'processo/update.html'
    form_class = UpdateForm
    raiz = "Prestação de Serviços"
    titulo = "Editar Prestação de Serviços"
    url_prefix = "processos"


class ProcessoDelete(CustomDeleteView):
    class DeleteForm(ProcessoForm):
        class Meta:
            model = Processo
            fields = '__all__'

    model = Processo
    template_name = 'processo/delete.html'
    raiz = "Prestação de Serviços"
    titulo = "Deletar Prestação de Serviços"
    descricao = "Prestação de Serviços"
    url_prefix = "processos"
    form_class = DeleteForm

