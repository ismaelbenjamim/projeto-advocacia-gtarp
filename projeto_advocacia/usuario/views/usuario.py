from django import forms
from django.contrib.auth.hashers import make_password
from django.urls import reverse_lazy

from projeto_advocacia.core.forms import CustomModelForm
from projeto_advocacia.core.views import CustomListView, CustomDetailView, CustomCreateView, CustomUpdateView, \
    CustomDeleteView
from projeto_advocacia.usuario.models import Usuario, Cliente


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control mb-2'


class UsuarioCreateForm(UsuarioForm):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'cargo', 'celular', 'idade', 'organizacao']

    def clean(self):
        response = super(UsuarioCreateForm, self).clean()
        response['password'] = make_password(response['password'])
        return response

class UsuarioUpdateForm(UsuarioForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'cargo', 'celular', 'idade', 'organizacao', 'foto_perfil']


class UsuarioPerfilForm(UsuarioForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'celular', 'idade', 'organizacao', 'foto_perfil']


class UsuarioFilters(CustomModelForm):
    class Meta:
        model = Usuario
        fields = ['identidade', 'first_name', 'last_name', 'celular', 'idade', 'organizacao']


class UsuarioList(CustomListView):
    model = Usuario
    queryset = Usuario.objects.all()
    paginate_by = 10
    ordering = ['pk']
    template_name = 'usuario/list.html'
    raiz = "Usuários"
    titulo = "Lista de Usuários"
    url_prefix = "usuarios"
    fields = ['id', 'first_name', 'last_name', 'identidade', 'celular', 'idade', 'organizacao']
    filters_form = UsuarioFilters


class UsuarioDetail(CustomDetailView):
    model = Usuario
    template_name = 'usuario/detail.html'
    raiz = "Usuários"
    titulo = "Detalhe do Usuário"
    url_prefix = "usuarios"
    form_class = UsuarioUpdateForm


class UsuarioCreate(CustomCreateView):
    model = Usuario
    template_name = 'usuario/create.html'
    form_class = UsuarioCreateForm
    raiz = "Usuários"
    titulo = "Adicionar novo Usuário"
    url_prefix = "usuarios"


class UsuarioUpdate(CustomUpdateView):
    model = Usuario
    template_name = 'usuario/update.html'
    form_class = UsuarioUpdateForm
    raiz = "Usuários"
    titulo = "Editar Usuário"
    url_prefix = "usuarios"


class UsuarioDelete(CustomDeleteView):
    model = Usuario
    template_name = 'usuario/delete.html'
    raiz = "Usuários"
    titulo = "Deletar Usuário"
    descricao = "Usuário"
    url_prefix = "usuarios"
    form_class = UsuarioUpdateForm


class UsuarioPerfil(CustomUpdateView):
    model = Usuario
    template_name = 'usuario/update.html'
    form_class = UsuarioPerfilForm
    raiz = "Usuarios"
    titulo = "Editar Usuario"
    campos_filtro = ['first_name', 'last_name', 'celular', 'idade', 'organizacao', 'foto_perfil']

    def get_success_url(self):
        return reverse_lazy("usuarios_list", {"pk": self.object.pk})
