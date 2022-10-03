from django import forms
from django.contrib.auth import authenticate, login
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
            if visible.field.__class__.__name__ == "BooleanField":
                visible.field.widget.attrs['class'] = 'form-check-input mb-2'
            else:
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
    class UsuarioPerfilForm(UsuarioForm):
        class Meta:
            model = Usuario
            fields = ['foto_perfil', 'first_name', 'last_name', 'celular', 'idade']

    model = Usuario
    template_name = 'usuario/perfil.html'
    raiz = "Usuarios"
    titulo = "Editar Usuario"
    url_prefix = "usuarios"
    form_class = UsuarioPerfilForm

    def setup(self, request, *args, **kwargs):
        super(UsuarioPerfil, self).setup(request, *args, **kwargs)
        self.kwargs = {'pk': str(self.request.user.pk)}

    def get_success_url(self):
        return reverse_lazy("usuarios_perfil")


class UsuarioChangePassword(CustomUpdateView):
    class UsuarioPasswordForm(UsuarioForm):
        password_now = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-2'}), required=True)
        password_new = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-2'}), required=True)
        class Meta:
            model = Usuario
            fields = ['password']

        def clean(self):
            response = super().clean()
            check_password = authenticate(username=self.instance.username, password=response['password_now'])
            if check_password is not None:
                if not response['password'] == response['password_new']:
                    self.add_error("password_new", "A confirmação de senha não coincide com a nova senha")
                else:
                    response['password'] = make_password(response['password'])
            else:
                self.add_error("password_now", "A senha atual está incorreta")

    model = Usuario
    template_name = 'usuario/change_password.html'
    raiz = "Usuarios"
    titulo = "Alterar Senha"
    url_prefix = "usuarios"
    form_class = UsuarioPasswordForm

    def setup(self, request, *args, **kwargs):
        super(UsuarioChangePassword, self).setup(request, *args, **kwargs)
        self.kwargs = {'pk': str(self.request.user.pk)}

    def form_valid(self, form):
        return super(UsuarioChangePassword, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy("login")
