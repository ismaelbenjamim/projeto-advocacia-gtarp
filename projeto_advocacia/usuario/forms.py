from django import forms

from projeto_advocacia.processo.models import Processo, Lei, PrestacaoServico
from projeto_advocacia.usuario.models import Cliente, Usuario, Servico


class UsuarioForm(forms.ModelForm):
    autor = forms.ModelChoiceField(queryset=Cliente.objects.all(),
                                   widget=forms.TextInput(attrs={'list': 'list_autor'}),  to_field_name='identidade')
    reu = forms.ModelChoiceField(queryset=Cliente.objects.all(),
                                 widget=forms.TextInput(attrs={'list': 'list_reu'}), to_field_name='identidade')
    juiz = forms.ModelChoiceField(queryset=Usuario.objects.all(), required=False,
                                  widget=forms.TextInput(attrs={'list': 'list_juiz'}), to_field_name='identidade')
    advogado_autor = forms.ModelChoiceField(queryset=Usuario.objects.all(), required=False,
                                            widget=forms.TextInput(attrs={'list': 'list_adv_autor'}), to_field_name='identidade')
    advogado_reu = forms.ModelChoiceField(queryset=Usuario.objects.all(), required=False,
                                          widget=forms.TextInput(attrs={'list': 'list_adv_reu'}), to_field_name='identidade')
    provas_autor = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    provas_reu = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Usuario
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control mb-2'


class UsuarioPerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'celular', 'idade', 'organizacao', 'foto_perfil']

    def __init__(self, *args, **kwargs):
        super(UsuarioPerfilForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control mb-2'


class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['id', 'descricao', 'valor_base', 'cargo_responsavel', 'is_ativo']

    def __init__(self, *args, **kwargs):
        super(ServicoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.field.__class__.__name__ == "BooleanField":
                visible.field.widget.attrs['class'] = 'form-check-input mb-2'
            else:
                visible.field.widget.attrs['class'] = 'form-control mb-2'


class PrestacaoServicoForm(forms.ModelForm):
    class Meta:
        model = PrestacaoServico
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PrestacaoServicoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control mb-2'


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control mb-2'