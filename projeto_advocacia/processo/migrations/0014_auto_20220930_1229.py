# Generated by Django 3.2.15 on 2022-09-30 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processo', '0013_auto_20220930_1227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lei',
            name='tipo',
        ),
        migrations.AddField(
            model_name='lei',
            name='categoria',
            field=models.CharField(choices=[('1', 'Código penal'), ('2', 'Contravenções penais'), ('3', 'Código de processo penal'), ('4', 'Crimes do sistema nacional de armas'), ('5', 'Crimes do sistema nacional de políticas públicas sobre Drogas'), ('6', 'Código de Trânsito Brasileiro'), ('7', 'Abuso de Autoridade'), ('8', 'Lavagem de dinheiro')], default=1, max_length=200, verbose_name='Categoria'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='processo',
            name='numero_processo',
            field=models.CharField(default='435552655', max_length=20, verbose_name='Número do processo'),
        ),
    ]
