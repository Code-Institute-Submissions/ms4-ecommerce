# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-26 19:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_ratings', '0024_auto_20200726_1821'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewlineitem',
            old_name='new_item',
            new_name='object',
        ),
        migrations.RemoveField(
            model_name='reviewlineitem',
            name='product',
        ),
    ]
