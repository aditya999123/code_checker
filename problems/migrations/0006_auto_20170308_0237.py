# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-08 02:37
from __future__ import unicode_literals

from django.db import migrations, models
import problems.models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0005_group_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problems',
            name='problem_code',
            field=models.CharField(max_length=6, unique=True, validators=[problems.models.validate_len]),
        ),
    ]
