# Generated by Django 4.0.5 on 2022-07-01 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_alter_usuario_cpf_cnpj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='cpf_cnpj',
            field=models.CharField(max_length=18, unique=True, verbose_name='CPF/CNPJ'),
        ),
    ]
