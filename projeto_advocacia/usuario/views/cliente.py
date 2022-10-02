from django.urls import reverse_lazy
from projeto_advocacia.core.views import CustomListView, CustomDetailView, CustomCreateView, CustomUpdateView, \
    CustomDeleteView
from projeto_advocacia.usuario.forms import ClienteForm
from projeto_advocacia.usuario.models import Cliente


class ClienteList(CustomListView):
    model = Cliente
    queryset = Cliente.objects.all()
    paginate_by = 10
    ordering = ['pk']
    template_name = 'cliente/list.html'
    raiz = "Clientes"
    titulo = "Lista de Clientes"
    fields = ['identidade', 'nome', 'sobrenome', 'celular', 'idade', 'status', 'organizacao', 'porte', 'cnh']

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
        queryset = super(ClienteList, self).get_queryset()
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


class ClienteDetail(CustomDetailView):
    model = Cliente
    template_name = 'cliente/detail.html'
    raiz = "Clientes"
    titulo = "Detalhe do Cliente"
    campos_tabela = model._meta.get_fields()
    url_raiz = 'clientes'


class ClienteCreate(CustomCreateView):
    model = Cliente
    template_name = 'cliente/create.html'
    form_class = ClienteForm
    success_url = reverse_lazy("clientes_list")
    raiz = "Clientes"
    titulo = "Adicionar novo Cliente"


class ClienteUpdate(CustomUpdateView):
    model = Cliente
    template_name = 'cliente/update.html'
    form_class = ClienteForm
    raiz = "Clientes"
    titulo = "Editar Cliente"
    campos_filtro = ['autor', 'reu', 'juiz', 'advogado_autor', 'advogado_reu']

    def get_success_url(self):
        success_url = reverse_lazy(f"clientes_detail", kwargs={"pk": self.object.pk})
        return success_url

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        response = form_class(**self.get_form_kwargs())
        for field in response:
            if field.name in self.campos_filtro:
                field.initial = getattr(self.object, field.name)
        return response


class ClienteDelete(CustomDeleteView):
    model = Cliente
    template_name = 'cliente/delete.html'
    success_url = reverse_lazy("clientes_list")
    raiz = "Clientes"
    titulo = "Deletar Cliente"
    descricao = "Clientes"
    campos_tabela = model._meta.get_fields()