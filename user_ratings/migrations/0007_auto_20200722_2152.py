# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-22 21:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200604_1359'),
        ('user_ratings', '0006_auto_20200722_2138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='id',
        ),
        migrations.AddField(
            model_name='item',
            name='product',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='products.Product'),
        ),
    ]