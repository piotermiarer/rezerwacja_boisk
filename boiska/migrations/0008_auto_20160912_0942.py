# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-12 07:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boiska', '0007_auto_20160912_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportsground',
            name='end_season_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='sportsground',
            name='start_season_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
