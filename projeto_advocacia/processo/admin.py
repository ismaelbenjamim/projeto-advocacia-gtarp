from django.contrib import admin

from projeto_advocacia.processo.models import Processo, Lei

admin.site.register(Processo)
admin.site.register(Lei)
