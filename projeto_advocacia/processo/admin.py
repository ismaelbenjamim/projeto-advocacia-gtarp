from django.contrib import admin

from projeto_advocacia.processo.models import Processo, Lei, ServicoLeis

admin.site.register(Processo)
admin.site.register(Lei)
admin.site.register(ServicoLeis)
