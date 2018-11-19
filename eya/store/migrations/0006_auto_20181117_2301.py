# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-17 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20180916_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailorder',
            name='discount',
            field=models.PositiveIntegerField(default=0, verbose_name='Descuento'),
        ),
        migrations.AlterField(
            model_name='detailorder',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Precio'),
        ),
    ]
