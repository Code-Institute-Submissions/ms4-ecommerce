# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-21 11:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200604_1359'),
        ('user_ratings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
    ]