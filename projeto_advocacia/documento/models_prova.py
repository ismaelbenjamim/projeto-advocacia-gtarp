from django.db import models

from projeto_advocacia.documento.models import Documento
from projeto_advocacia.processo.models import Processo
from projeto_advocacia.usuario.models import Usuario


class Prova(models.Model):
    responsavel = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    descricao = models.TextField(verbose_name='Descrição', null=True, blank=True)
    processo = models.ForeignKey(Processo, on_delete=models.CASCADE)
    documento = models.ForeignKey(Documento, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.processo} - {self.responsavel}'
