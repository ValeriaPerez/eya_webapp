# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-01-13 05:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20190104_0104'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=200, verbose_name='Categoria'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Cantidad'),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity_descr',
            field=models.CharField(default='', max_length=200, verbose_name='Cantidad descripci\xf3n'),
            preserve_default=False,
        ),
    ]
