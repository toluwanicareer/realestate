# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-18 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_property_avetiz_agent'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='feature',
            field=models.BooleanField(default=False),
        ),
    ]
