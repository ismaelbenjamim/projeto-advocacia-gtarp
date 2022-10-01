from django.contrib import admin

from projeto_advocacia.documento.models import Documento
from projeto_advocacia.documento.models_prova import Prova

admin.site.register(Documento)
admin.site.register(Prova)
