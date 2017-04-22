# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-21 23:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_hour_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignmentsubmission',
            old_name='submission',
            new_name='submission_type',
        ),
        migrations.AddField(
            model_name='assignmentsubmission',
            name='body',
            field=models.TextField(null=True),
        ),
    ]
