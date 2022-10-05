import random

from django.db import models

from projeto_advocacia.usuario.models import Usuario, Cliente, Servico


def gerar_numero_processo(num=""):
    for i in range(0, 9):
        n = random.randint(1, 9)
        num = num + str(n)
    return num


class Processo(models.Model):
    TIPOS_FASES = (
        ('postulatoria', 'Postulatória'),
        ('instrutoria', 'Instrutória'),
        ('decisoria', 'Decisória'),
        ('recursal', 'Recursal'),
        ('executiva', 'Executiva')
    )
    TIPOS_PROCESSOS = (
        ('conhecimento', 'Conhecimento'),
        ('cautelar', 'Cautelar'),
        ('execução', 'Execução')
    )
    numero_processo = models.CharField(verbose_name="Número do processo", default=gerar_numero_processo, max_length=20)
    autor = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='autor', verbose_name="Autor")
    reu = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='reu', verbose_name="Réu")
    juiz = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True,
                             related_name='juiz', verbose_name='Juiz')
    advogado_autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True,
                                       blank=True, related_name='advogado_autor', verbose_name="Advogado do autor")
    advogado_reu = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True,
                                     blank=True, related_name='advogado_reu', verbose_name="Advogado do Réu")
    data_abertura = models.DateField('Data de abertura', null=True, blank=True)
    fase = models.CharField('Fase', max_length=100, choices=TIPOS_FASES)
    tipo = models.CharField('Tipo', max_length=100, choices=TIPOS_PROCESSOS)
    descricao = models.TextField('Descrição do processo', null=True, blank=True)
    postulatoria = models.TextField('Descrição da fase Postulatória', null=True, blank=True)
    instrutoria = models.TextField('Descrição do fase Instrutória', null=True, blank=True)
    decisoria = models.TextField('Descrição do fase Decisória', null=True, blank=True)
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
    categoria = models.CharField('Categoria', max_length=200, choices=TIPOS_LEIS)
    artigo = models.CharField('Artigo', max_length=200)
    descricao = models.CharField('Descrição', max_length=255)
    pena_base_multa = models.DecimalField('Multa de pena', max_digits=15, decimal_places=2, default=0)
    pena_base_meses = models.IntegerField('Meses da pena', default=0)
    pena_fianca = models.DecimalField('Fiança', max_digits=15, decimal_places=2, null=True, blank=True)
    pena_agravante = models.CharField('Agravante', max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.get_categoria_display()} - {self.artigo}'


class PrestacaoServico(models.Model):
    responsavel = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, verbose_name='Resposável')
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, verbose_name='Serviço')
    descricao = models.TextField(verbose_name='Descrição do serviço prestado', null=True, blank=True)
    valor = models.DecimalField(verbose_name="Valor", max_digits=15, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    processo = models.ForeignKey(Processo, on_delete=models.CASCADE, null=True, blank=True)
    pena_cliente = models.TextField(verbose_name='Pena do cliente', max_length=200, null=True, blank=True)


class ServicoLeis(models.Model):
    servico = models.ForeignKey(PrestacaoServico, on_delete=models.CASCADE)
    leis = models.ForeignKey(Lei, on_delete=models.CASCADE)
