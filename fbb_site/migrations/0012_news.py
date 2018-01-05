# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-04 22:59
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('fbb_site', '0011_auto_20171229_2135'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=350)),
                ('abstract', models.CharField(max_length=700)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('content', tinymce.models.HTMLField()),
            ],
        ),
    ]
