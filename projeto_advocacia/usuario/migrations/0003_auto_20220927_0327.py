# Generated by Django 3.2.15 on 2022-09-27 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_auto_20220927_0104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='passaporte',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='passaporte',
        ),
        migrations.AddField(
            model_name='cliente',
            name='identidade',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='identidade'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='identidade',
            field=models.CharField(default=1, max_length=10, verbose_name='Identidade'),
            preserve_default=False,
        ),
    ]
