# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-13 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='time',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=8),
        ),
    ]
