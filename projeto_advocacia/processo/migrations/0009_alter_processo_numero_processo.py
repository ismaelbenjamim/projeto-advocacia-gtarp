# Generated by Django 3.2.15 on 2022-09-28 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processo', '0008_alter_processo_numero_processo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processo',
            name='numero_processo',
            field=models.CharField(default='256975589', max_length=20),
        ),
    ]