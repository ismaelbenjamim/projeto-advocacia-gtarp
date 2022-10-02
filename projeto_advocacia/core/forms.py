from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.core.validators import RegexValidator
from django.utils.regex_helper import _lazy_re_compile

from projeto_advocacia.usuario.models import Usuario


integer_validator = RegexValidator(
    _lazy_re_compile(r'^-?\d+\Z'),
    message='A identidade é representada por valores numéricos, ex: 1234',
    code='invalid',
)
def validate_integer(value):
    return integer_validator(value)

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="Identidade",
        widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}),
        validators=[validate_integer]
    )
    password = forms.CharField(
        label="Senha",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}),
    )

    error_messages = {
        'invalid_login': (
            "Usuário ou senha estão incorretos."
        ),
        'inactive': "Esta conta está inativa",
    }

    def clean(self):
        identidade = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if identidade is not None and password:
            user = Usuario.objects.filter(identidade=identidade)
            username = user.first().username if user else None
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data
