import random

from django.db import models

from projeto_advocacia.usuario.models import Usuario, Cliente


def gerar_numero_processo(num=""):
    for i in range(0, 9):
        n = random.randint(1, 9)
        num = num + str(n)
    return num


class Processo(models.Model):
    TIPOS_FASES = (
        ('Postulatória', 'Postulatória'),
        ('Instrutória', 'Instrutória'),
        ('Decisória', 'Decisória'),
        ('Recursal', 'Recursal'),
        ('Executiva', 'Executiva')
    )
    TIPOS_PROCESSOS = (
        ('Conhecimento', 'Conhecimento'),
        ('Cautelar', 'Cautelar'),
        ('Execução', 'Execução')
    )
    numero_processo = models.CharField(default=gerar_numero_processo(), max_length=20)
    autor = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='autor')
    reu = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='reu')
    juiz = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True, related_name='juiz')
    advogado_autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True, related_name='advogado_autor')
    advogado_reu = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True, related_name='advogado_reu')
    data_abertura = models.DateField('Data de abertura', null=True, blank=True)
    fase = models.CharField('Fase', max_length=100, choices=TIPOS_FASES)
    tipo = models.CharField('Tipo', max_length=100, choices=TIPOS_PROCESSOS)
    descricao = models.TextField('Descrição do processo', null=True, blank=True)
    postulatoria = models.TextField('Descrição da fase Postulatória', null=True, blank=True)
    instrutória = models.TextField('Descrição do fase Instrutória', null=True, blank=True)
    decisória = models.TextField('Descrição do fase Decisória', null=True, blank=True)
    recursal = models.TextField('Descrição do fase Recursal', null=True, blank=True)
    executiva = models.TextField('Descrição do fase Executiva', null=True, blank=True)


    def __str__(self):
        return f'{self.numero_processo}'


class Lei(models.Model):
    TIPOS_LEIS = (
        ('1', 'Código penal'),
        ('2', 'Contravenções penais'),
        ('3', 'Código de processo penal'),
        ('4', 'Crimes do sistema nacional de armas'),
        ('5', 'Crimes do sistema nacional de políticas públicas sobre Drogas'),
        ('6', 'Código de Trânsito Brasileiro'),
        ('7', 'Abuso de Autoridade'),
        ('8', 'Lavagem de dinheiro'),
    )
    tipo = models.CharField('Tipo', max_length=200, choices=TIPOS_LEIS)
    artigo = models.CharField('Artigo', max_length=10)
    descricao = models.TextField('Descrição')
    pena_base = models.CharField('Pena base', max_length=255)
    pena_fianca = models.CharField('Fiança', max_length=255)
    pena_agravante = models.TextField('Agravante')
