from django import forms
from projeto_advocacia.core.forms import CustomModelForm
from projeto_advocacia.core.views import CustomListView, CustomDetailView, CustomCreateView, CustomUpdateView, \
    CustomDeleteView
from projeto_advocacia.documento.models import Documento


class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.field.__class__.__name__ == "BooleanField":
                visible.field.widget.attrs['class'] = 'form-check-input mb-2'
            else:
                visible.field.widget.attrs['class'] = 'form-control mb-2'


class DocumentoList(CustomListView):
    class FiltersForm(CustomModelForm):
        class Meta:
            model = Documento
            fields = ['descricao', 'responsavel', 'tipo', 'documento_gerado_modelo']

    model = Documento
    queryset = Documento.objects.all()
    paginate_by = 10
    ordering = ['pk']
    template_name = 'documento/list.html'
    raiz = "Documentos"
    titulo = "Lista de Documentos"
    url_prefix = "documentos"
    fields = ['descricao', 'responsavel', 'tipo', 'documento_gerado_modelo', 'documento_submetido']
    filters_form = FiltersForm


class DocumentoDetail(CustomDetailView):
    class DetailForm(DocumentoForm):
        class Meta:
            model = Documento
            fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['disabled'] = True

    model = Documento
    template_name = 'documento/detail.html'
    raiz = "Documentos"
    titulo = "Detalhe do Documento"
    url_prefix = "documentos"
    form_class = DetailForm


class DocumentoCreate(CustomCreateView):
    class CreateForm(DocumentoForm):
        class Meta:
            model = Documento
            fields = '__all__'

    model = Documento
    template_name = 'documento/create.html'
    form_class = CreateForm
    raiz = "Documentos"
    titulo = "Adicionar novo Documento"
    url_prefix = "documentos"


class DocumentoUpdate(CustomUpdateView):
    class UpdateForm(DocumentoForm):
        class Meta:
            model = Documento
            fields = '__all__'

    model = Documento
    template_name = 'documento/update.html'
    form_class = UpdateForm
    raiz = "Documentos"
    titulo = "Editar Documento"
    url_prefix = "documentos"


class DocumentoDelete(CustomDeleteView):
    class DeleteForm(DocumentoForm):
        class Meta:
            model = Documento
            fields = '__all__'

    model = Documento
    template_name = 'documento/delete.html'
    raiz = "Documentos"
    titulo = "Deletar Documento"
    descricao = "Documento"
    url_prefix = "documentos"
    form_class = DeleteForm

