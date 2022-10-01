from django import forms

from projeto_advocacia.documento.models import Documento
from projeto_advocacia.usuario.models import Usuario


class DocumentoForm(forms.ModelForm):
    responsavel = forms.ModelChoiceField(queryset=Usuario.objects.all(),
                                   widget=forms.TextInput(attrs={'list': 'list_responsavel'}), to_field_name='identidade')
    documento_submetido = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Documento
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DocumentoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control mb-2'
