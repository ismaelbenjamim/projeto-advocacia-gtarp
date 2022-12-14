from django import forms

from projeto_advocacia.processo.models import Processo, Lei
from projeto_advocacia.usuario.models import Cliente, Usuario


class ProcessoForm(forms.ModelForm):
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
        model = Processo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProcessoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control mb-2'


class LeiForm(forms.ModelForm):
    class Meta:
        model = Lei
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(LeiForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control mb-2'
