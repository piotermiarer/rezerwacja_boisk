# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-11 18:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boiska', '0002_auto_20160908_2114'),
    ]

    operations = [
        migrations.CreateModel(
            name='SportsGround',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
                ('start_season_date', models.DateTimeField(blank=True)),
                ('end_season_date', models.DateTimeField(blank=True)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sports_grounds', to='boiska.Place')),
            ],
        ),
    ]
