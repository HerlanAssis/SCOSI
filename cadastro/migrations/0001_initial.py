# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-14 19:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
            ],
            options={
                'ordering': ('nome',),
                'verbose_name': 'bairro',
                'verbose_name_plural': 'bairros',
                'permissions': (('pode_ver', 'Pode ver'), ('pode_adicionar', 'Pode adicionar'), ('pode_editar', 'Pode editar'), ('pode_excluir', 'Pode excluir')),
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, verbose_name='nome')),
                ('sobrenome', models.CharField(max_length=30, verbose_name='sobrenome')),
                ('cpf', models.BigIntegerField(unique=True, verbose_name='CPF')),
            ],
        ),
        migrations.CreateModel(
            name='Logradouro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='logradouro')),
                ('bairro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.Bairro')),
            ],
            options={
                'ordering': ('bairro', 'nome'),
                'verbose_name': 'logradouro',
                'verbose_name_plural': 'logradouros',
                'permissions': (('pode_ver', 'Pode ver'), ('pode_adicionar', 'Pode adicionar'), ('pode_editar', 'Pode editar'), ('pode_excluir', 'Pode excluir')),
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('nome',),
                'verbose_name': 'munic\xedpio',
                'verbose_name_plural': 'munic\xedpios',
                'permissions': (('pode_ver', 'Pode ver'), ('pode_adicionar', 'Pode adicionar'), ('pode_editar', 'Pode editar'), ('pode_excluir', 'Pode excluir')),
            },
        ),
        migrations.CreateModel(
            name='UF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sigla', models.CharField(max_length=3)),
            ],
            options={
                'ordering': ('nome',),
                'verbose_name': 'estado',
                'verbose_name_plural': 'estados',
                'permissions': (('pode_ver', 'Pode ver'), ('pode_adicionar', 'Pode adicionar'), ('pode_editar', 'Pode editar'), ('pode_excluir', 'Pode excluir')),
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.PositiveIntegerField(choices=[(1, 'Supervisor'), (2, 'Secretario'), (3, 'T\xe9cnico')], default=1, verbose_name='tipo de usu\xe1rio')),
                ('cpf', models.BigIntegerField(unique=True, verbose_name='CPF')),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.Logradouro', verbose_name='endere\xe7o')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='usu\xe1rio')),
            ],
            options={
                'verbose_name': 'usu\xe1rio',
                'verbose_name_plural': 'usu\xe1rios',
                'permissions': (('pode_ver', 'Pode ver'), ('pode_adicionar', 'Pode adicionar'), ('pode_editar', 'Pode editar'), ('pode_excluir', 'Pode excluir')),
            },
        ),
        migrations.AddField(
            model_name='municipio',
            name='uf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.UF', verbose_name='UF'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='endereco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.Logradouro', verbose_name='endere\xe7o'),
        ),
        migrations.AddField(
            model_name='bairro',
            name='municipio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bairros', to='cadastro.Municipio', verbose_name='munic\xedpio'),
        ),
    ]