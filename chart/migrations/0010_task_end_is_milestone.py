# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-15 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0009_schedule_selected_row'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='end_is_milestone',
            field=models.BooleanField(default=False),
        ),
    ]