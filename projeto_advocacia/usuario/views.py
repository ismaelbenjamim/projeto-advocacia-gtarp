from django.urls import reverse_lazy
from projeto_advocacia.core.views import CustomListView, CustomDetailView, CustomCreateView, CustomUpdateView, \
    CustomDeleteView
from projeto_advocacia.processo.models import PrestacaoServico
from projeto_advocacia.usuario.forms import UsuarioForm, ServicoForm, PrestacaoServicoForm, ClienteForm
from projeto_advocacia.usuario.models import Usuario, Servico, Cliente


class UsuarioList(CustomListView):
    model = Usuario
    queryset = Usuario.objects.all()
    paginate_by = 10
    ordering = ['pk']
    template_name = 'usuario/list.html'
    raiz = "Usuarios"
    titulo = "Lista de Usuarios"
    campos_tabela = ['Identidade', 'Cargo', 'Nome', 'Sobrenome', 'Celular', 'Idade']

    def get_queryset(self):
        queryset = super(UsuarioList, self).get_queryset()
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


class UsuarioDetail(CustomDetailView):
    model = Usuario
    template_name = 'usuario/detail.html'
    raiz = "Usuarios"
    titulo = "Detalhe do Usuario"
    fields = ['id', 'identidade', 'username', 'email', 'first_name', 'last_name', 'idade', 'cargo',
                     'last_login', 'date_joined']
    #campos_filtro = ['descricao', 'postulatoria', 'instrutoria', 'decisoria', 'recursal', 'executiva']

    def campos_tabela(self):
        fields = []
        for field in self.object._meta.get_fields():
            if field.name in self.fields:
                fields.append(field)
        return fields


class UsuarioCreate(CustomCreateView):
    model = Usuario
    template_name = 'usuario/create.html'
    form_class = UsuarioForm
    success_url = reverse_lazy("usuarios_list")
    raiz = "Usuarios"
    titulo = "Adicionar novo usuario"


class UsuarioUpdate(CustomUpdateView):
    model = Usuario
    template_name = 'usuario/update.html'
    form_class = UsuarioForm
    raiz = "Usuarios"
    titulo = "Editar Usuario"
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
        return reverse_lazy("usuarios_list", {"pk": self.object.pk})


class UsuarioDelete(CustomDeleteView):
    model = Usuario
    queryset = Usuario.objects.all()
    template_name = 'usuario/delete.html'
    form_class = UsuarioForm
    success_url = reverse_lazy("usuarios_list")
    raiz = "Usuarios"
    titulo = "Deletar Usuario"
    descricao = "Usuario"
    campos_tabela = ['data_abertura', 'autor', 'reu', 'juiz', 'advogado_autor', 'advogado_reu', 'fase']


# ------------------------------------------- CLIENTE -------------------------------------------#
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


# ------------------------------------------- SERVICOS -------------------------------------------#
class ServicoList(CustomListView):
    model = Servico
    queryset = Servico.objects.all()
    paginate_by = 10
    ordering = ['pk']
    template_name = 'servico/list.html'
    raiz = "Serviços"
    titulo = "Lista de Serviços"
    fields = ['id', 'descricao', 'valor_base', 'cargo_responsavel', 'is_ativo']

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
        queryset = super(ServicoList, self).get_queryset()
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


class ServicoDetail(CustomDetailView):
    model = Servico
    template_name = 'servico/detail.html'
    raiz = "Serviços"
    titulo = "Detalhe do Serviço"
    campos_tabela = model._meta.get_fields()


class ServicoCreate(CustomCreateView):
    model = Servico
    template_name = 'servico/create.html'
    form_class = ServicoForm
    success_url = reverse_lazy("servicos_list")
    raiz = "Serviços"
    titulo = "Adicionar novo Serviço"


class ServicoUpdate(CustomUpdateView):
    model = Servico
    template_name = 'servico/update.html'
    form_class = ServicoForm
    raiz = "Serviços"
    titulo = "Editar Serviço"
    campos_filtro = ['autor', 'reu', 'juiz', 'advogado_autor', 'advogado_reu']

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
    success_url = reverse_lazy("servicos_list")
    raiz = "Serviços"
    titulo = "Deletar Serviço"
    descricao = "Serviço"
    campos_tabela = model._meta.get_fields()
# ------------------------------------------- SERVICOS -------------------------------------------#


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
