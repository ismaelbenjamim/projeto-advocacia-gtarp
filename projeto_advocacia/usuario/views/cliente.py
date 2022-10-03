from django import forms
from projeto_advocacia.core.forms import CustomModelForm
from projeto_advocacia.core.views import CustomListView, CustomDetailView, CustomCreateView, CustomUpdateView, \
    CustomDeleteView
from projeto_advocacia.usuario.models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.field.__class__.__name__ == "BooleanField":
                visible.field.widget.attrs['class'] = 'form-check-input mb-2'
            else:
                visible.field.widget.attrs['class'] = 'form-control mb-2'


class ClienteList(CustomListView):
    class FiltersForm(CustomModelForm):
        class Meta:
            model = Cliente
            fields = ['nome', 'sobrenome', 'identidade', 'celular', 'idade', 'status', 'organizacao', 'porte', 'cnh']

    model = Cliente
    queryset = Cliente.objects.all()
    paginate_by = 10
    ordering = ['pk']
    template_name = 'cliente/list.html'
    raiz = "Clientes"
    titulo = "Lista de Clientes"
    url_prefix = "clientes"
    fields = ['id', 'nome', 'sobrenome', 'identidade', 'celular', 'idade', 'status', 'organizacao', 'porte', 'cnh']
    filters_form = FiltersForm


class ClienteDetail(CustomDetailView):
    class DetailForm(ClienteForm):
        class Meta:
            model = Cliente
            fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['disabled'] = True

    model = Cliente
    template_name = 'cliente/detail.html'
    raiz = "Clientes"
    titulo = "Detalhe do Cliente"
    url_prefix = "clientes"
    form_class = DetailForm


class ClienteCreate(CustomCreateView):
    class CreateForm(ClienteForm):
        class Meta:
            model = Cliente
            fields = '__all__'

    model = Cliente
    template_name = 'cliente/create.html'
    form_class = CreateForm
    raiz = "Clientes"
    titulo = "Adicionar novo Cliente"
    url_prefix = "clientes"


class ClienteUpdate(CustomUpdateView):
    class UpdateForm(ClienteForm):
        class Meta:
            model = Cliente
            fields = '__all__'

    model = Cliente
    template_name = 'cliente/update.html'
    form_class = UpdateForm
    raiz = "Clientes"
    titulo = "Editar Cliente"
    url_prefix = "clientes"


class ClienteDelete(CustomDeleteView):
    class DeleteForm(ClienteForm):
        class Meta:
            model = Cliente
            fields = '__all__'

    model = Cliente
    template_name = 'cliente/delete.html'
    raiz = "Clientes"
    titulo = "Deletar Cliente"
    descricao = "Cliente"
    url_prefix = "clientes"
    form_class = DeleteForm

