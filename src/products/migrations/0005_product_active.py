# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-02-13 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
