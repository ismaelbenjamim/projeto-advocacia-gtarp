# Generated by Django 3.2.15 on 2022-10-01 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processo', '0018_alter_processo_numero_processo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processo',
            name='numero_processo',
            field=models.CharField(default='422326555', max_length=20, verbose_name='Número do processo'),
        ),
    ]
