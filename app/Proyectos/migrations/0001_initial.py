# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 00:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Investigador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='proyectos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=25)),
                ('Documento', models.FileField(upload_to=b'')),
                ('Tipo_Proyecto', models.CharField(max_length=15)),
                ('investigador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Investigador.investigador')),
            ],
        ),
    ]
