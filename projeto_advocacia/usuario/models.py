from django.contrib.auth.models import AbstractUser
from django.db import models


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=250, blank=True)
    sobrenome = models.CharField('Sobrenome', max_length=250, blank=True)
    identidade = models.IntegerField('Identidade', unique=True, null=True, blank=True)
    celular = models.CharField('Celular', max_length=10, null=True, blank=True)
    idade = models.IntegerField('Idade', null=True, blank=True)
    status = models.CharField('Status', max_length=100, null=True, blank=True)
    organizacao = models.CharField('Organização', max_length=100, null=True, blank=True)
    porte = models.BooleanField('Porte', null=True, blank=True)
    cnh = models.BooleanField('CNH', null=True, blank=True)

    def __str__(self):
        return f'{self.nome} {self.sobrenome} #{self.identidade}'

    def get_nome_identidade(self):
        return self.__str__()

    def get_nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


class Usuario(AbstractUser):
    TIPOS_CARGOS = (
        ('0', 'Cliente'),
        ('1', 'Membro'),
        ('2', 'Advogado'),
        ('3', 'Promotor'),
        ('4', 'Juiz'),
        ('5', 'Juiz-Diretor'),
    )
    TIPOS_ORGS = (
        ('0', 'Policia Militar'),
        ('1', 'Polícia Civil'),
        ('2', 'Fórum'),
        ('3', 'Prefeitura'),
    )
    cargo = models.CharField('Cargo', max_length=20, choices=TIPOS_CARGOS, default='0')
    first_name = models.CharField('Nome', max_length=250, blank=True)
    last_name = models.CharField('Sobrenome', max_length=250, blank=True)
    identidade = models.IntegerField('Identidade', unique=True, null=True, blank=True)
    celular = models.CharField('Celular', max_length=10, null=True, blank=True)
    idade = models.IntegerField('Idade', null=True, blank=True)
    organizacao = models.CharField('Organização', max_length=100, choices=TIPOS_ORGS, null=True, blank=True)
    is_juridico = models.BooleanField('É do Fórum', default=False)
    foto_perfil = models.ImageField('Foto de perfil', null=True, blank=True)


    def __str__(self):
        if self.first_name and self.last_name:
            response = f'{self.first_name} {self.last_name} #{self.identidade}'
        else:
            response = f'{self.username}'
        return response

    def get_nome_identidade(self):
        return self.__str__()

    def get_nome_completo(self):
        if self.first_name and self.last_name:
            response = f'{self.first_name} {self.last_name}'
        else:
            response = f'{self.username}'
        return response


class Servico(models.Model):
    descricao = models.CharField("Descrição", max_length=250)
    valor_base = models.DecimalField("Valor do serviço", max_digits=15, decimal_places=2)
    cargo_responsavel = models.CharField("Cargo resposável", max_length=100, null=True, blank=True)
    is_ativo = models.BooleanField("É ativo", default=True)

    def __str__(self):
        return f'{self.descricao}'
