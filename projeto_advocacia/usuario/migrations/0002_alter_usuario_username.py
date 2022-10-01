# Generated by Django 3.2.15 on 2022-10-01 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='username',
            field=models.IntegerField(error_messages={'unique': 'Só pode existir um único usuário com essa identidade.'}, help_text='Requerido, são apenas números.', max_length=150, unique=True, verbose_name='Usuário'),
        ),
    ]
