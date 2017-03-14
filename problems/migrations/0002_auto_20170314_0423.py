# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-14 04:23
from __future__ import unicode_literals

from django.db import migrations, models
import problems.models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcase',
            name='expected_output',
            field=models.FileField(upload_to=problems.models.content_file_name),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='input',
            field=models.FileField(upload_to=problems.models.content_file_name),
        ),
    ]
