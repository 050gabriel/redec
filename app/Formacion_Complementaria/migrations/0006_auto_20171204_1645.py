# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 21:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Formacion_Complementaria', '0005_auto_20171123_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formacion_complementaria',
            name='investigador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Investigador.investigador'),
        ),
    ]
