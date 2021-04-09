# Generated by Django 3.1.7 on 2021-04-07 03:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0006_auto_20210406_2355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=150, verbose_name='Nomes')),
                ('surnames', models.CharField(max_length=150, verbose_name='Sobrenome')),
                ('rg', models.CharField(max_length=10, unique=True, verbose_name='RG')),
                ('birthday', models.DateField(default=datetime.datetime.now, verbose_name='Data de Nascimento')),
                ('address', models.CharField(blank=True, max_length=150, null=True, verbose_name='Endereço')),
                ('sexo', models.CharField(choices=[('male', 'Masculino'), ('female', 'Femenino')], default='male', max_length=10, verbose_name='Sexo')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['id'],
            },
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id'], 'verbose_name': 'Produto', 'verbose_name_plural': 'Produtos'},
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Nome'),
        ),
    ]
