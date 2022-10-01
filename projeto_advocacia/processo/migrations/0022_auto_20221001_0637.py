# Generated by Django 3.2.15 on 2022-10-01 06:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0010_auto_20221001_0637'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('processo', '0021_alter_processo_numero_processo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processo',
            name='numero_processo',
            field=models.CharField(default='866132944', max_length=20, verbose_name='Número do processo'),
        ),
        migrations.CreateModel(
            name='PrestacaoServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descrição do serviço prestado')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor')),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuario.cliente')),
                ('responsavel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Resposável')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.servico', verbose_name='Serviço')),
            ],
        ),
    ]