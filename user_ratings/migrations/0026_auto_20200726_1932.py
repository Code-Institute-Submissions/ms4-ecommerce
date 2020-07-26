# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-26 19:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200604_1359'),
        ('user_ratings', '0025_auto_20200726_1928'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewlineitem',
            old_name='object',
            new_name='item',
        ),
        migrations.AddField(
            model_name='item',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_id', to='products.Product'),
        ),
        migrations.AddField(
            model_name='reviewlineitem',
            name='product',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
    ]
