# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-02-13 19:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200213_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, default='abc', unique=True),
        ),
    ]
