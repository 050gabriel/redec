# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-21 17:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Datos_Profecionales', '0003_auto_20171120_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datos_profecionales',
            name='investigador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Investigador.investigador'),
        ),
    ]
