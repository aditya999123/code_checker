# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-07 03:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0003_problems_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='type',
            field=models.CharField(choices=[('PRACTICE', 'PRACTICE'), ('CONTEST', 'CONTEST'), ('LAB', 'LAB')], default='PRACTICE', max_length=100),
        ),
    ]
