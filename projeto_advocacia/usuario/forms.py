from django import forms

from projeto_advocacia.processo.models import Processo, Lei, PrestacaoServico
from projeto_advocacia.usuario.models import Cliente, Usuario, Servico


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