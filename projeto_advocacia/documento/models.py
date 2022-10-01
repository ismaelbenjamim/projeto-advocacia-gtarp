from django.core.exceptions import FieldError
from django.db import models

from projeto_advocacia.documento.utils.modelos import DocumentoModelo, TIPOS_MODELO_DUCUMENTO
from projeto_advocacia.usuario.models import Usuario


class Documento(models.Model):
    TIPOS_DOCUMENTO = (
        ('gerado', 'Documento gerado'),
        ('submetido', 'Documento submetido')
    )
    descricao = models.CharField("Descrição", max_length=250)
    responsavel = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    tipo = models.CharField("Tipo do documento", max_length=100, choices=TIPOS_DOCUMENTO)
    documento_gerado = models.JSONField("Documento gerado", null=True, blank=True)
    documento_gerado_modelo = models.CharField("Modelo do documento gerado", max_length=100,
                                               choices=TIPOS_MODELO_DUCUMENTO, null=True, blank=True)
    documento_submetido = models.FileField("Documento submetido", null=True, blank=True)

    def __str__(self):
        return f'{self.tipo} - {self.responsavel}'

    def validar_modelo(self):
        if not self.documento_gerado_modelo:
            raise FieldError('Campo documento_gerado_modelo não pode ser nulo.')
        modelo_serializer = DocumentoModelo.get_modelo(self.documento_gerado_modelo)
        serializer = modelo_serializer(data=self.documento_gerado)
        serializer.is_valid(raise_exception=True)
        self.documento_gerado = dict(serializer.data)
        return True

    def save(self, **kwargs):
        if self.tipo == 'gerado':
            self.documento_submetido = None
            self.validar_modelo()
        elif self.tipo == 'submetido':
            if not self.documento_submetido:
                raise FieldError('Campo documento_submetido não pode ser nulo.')
            self.documento_gerado = None
            self.documento_gerado_modelo = None
        else:
            raise FieldError('Campo tipo não pode ser nulo.')
        super(Documento, self).save()
