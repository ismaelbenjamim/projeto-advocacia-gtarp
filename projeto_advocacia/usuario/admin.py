from django.contrib import admin

from projeto_advocacia.usuario.models import Usuario, Cliente, Servico

admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(Servico)
