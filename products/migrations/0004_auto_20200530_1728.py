# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-30 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200530_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='info',
            field=models.CharField(default='', max_length=1200),
        ),
    ]