from django import forms
from projeto_advocacia.core.forms import CustomModelForm
from projeto_advocacia.core.views import CustomListView, CustomDetailView, CustomCreateView, CustomUpdateView, \
    CustomDeleteView
from projeto_advocacia.processo.models import Lei


class LeiForm(forms.ModelForm):
    class Meta:
        model = Lei
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.field.__class__.__name__ == "BooleanField":
                visible.field.widget.attrs['class'] = 'form-check-input mb-2'
            else:
                visible.field.widget.attrs['class'] = 'form-control mb-2'


class LeiList(CustomListView):
    class FiltersForm(CustomModelForm):
        class Meta:
            model = Lei
            fields = ['categoria', 'artigo', 'descricao']

    model = Lei
    queryset = Lei.objects.all()
    paginate_by = 10
    ordering = ['pk']
    template_name = 'legislacao/list.html'
    raiz = "Leis"
    titulo = "Lista de Leis"
    url_prefix = "leis"
    fields = ['categoria', 'artigo', 'descricao', 'pena_base_meses', 'pena_fianca', 'pena_agravante']
    filters_form = FiltersForm


class LeiDetail(CustomDetailView):
    class DetailForm(LeiForm):
        class Meta:
            model = Lei
            fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['disabled'] = True

    model = Lei
    template_name = 'legislacao/detail.html'
    raiz = "Leis"
    titulo = "Detalhe do Lei"
    url_prefix = "leis"
    form_class = DetailForm


class LeiCreate(CustomCreateView):
    class CreateForm(LeiForm):
        class Meta:
            model = Lei
            fields = '__all__'

    model = Lei
    template_name = 'legislacao/create.html'
    form_class = CreateForm
    raiz = "Leis"
    titulo = "Adicionar novo Lei"
    url_prefix = "leis"


class LeiUpdate(CustomUpdateView):
    class UpdateForm(LeiForm):
        class Meta:
            model = Lei
            fields = '__all__'

    model = Lei
    template_name = 'legislacao/update.html'
    form_class = UpdateForm
    raiz = "Leis"
    titulo = "Editar Lei"
    url_prefix = "leis"


class LeiDelete(CustomDeleteView):
    class DeleteForm(LeiForm):
        class Meta:
            model = Lei
            fields = '__all__'

    model = Lei
    template_name = 'legislacao/delete.html'
    raiz = "Leis"
    titulo = "Deletar Lei"
    descricao = "Lei"
    url_prefix = "leis"
    form_class = DeleteForm

