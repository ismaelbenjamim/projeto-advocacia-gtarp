# Generated by Django 3.2.15 on 2022-09-27 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processo',
            name='numero_processo',
            field=models.CharField(default='422712333', max_length=20),
        ),
    ]