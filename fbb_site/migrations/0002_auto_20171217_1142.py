# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-17 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbb_site', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lectorium',
            name='name',
            field=models.CharField(max_length=256),
        ),
    ]
