# Generated by Django 3.2.15 on 2022-09-30 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processo', '0014_auto_20220930_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processo',
            name='numero_processo',
            field=models.CharField(default='696932554', max_length=20, verbose_name='Número do processo'),
        ),
    ]
