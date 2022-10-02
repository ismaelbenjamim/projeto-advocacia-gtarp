from django.urls import reverse_lazy
from projeto_advocacia.core.views import CustomListView, CustomDetailView, CustomCreateView, CustomUpdateView, \
    CustomDeleteView
from projeto_advocacia.usuario.forms import UsuarioForm, UsuarioPerfilForm
from projeto_advocacia.usuario.models import Usuario


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
    campos_filtro = ['first_name', 'last_name', 'celular', 'idade', 'organizacao', 'foto_perfil']

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


class UsuarioPerfil(CustomUpdateView):
    model = Usuario
    template_name = 'usuario/update.html'
    form_class = UsuarioPerfilForm
    raiz = "Usuarios"
    titulo = "Editar Usuario"
    campos_filtro = ['first_name', 'last_name', 'celular', 'idade', 'organizacao', 'foto_perfil']

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
