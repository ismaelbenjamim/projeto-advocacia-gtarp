# Generated by Django 3.2.15 on 2022-09-27 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_auto_20220927_0327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='celular',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Celular'),
        ),
    ]