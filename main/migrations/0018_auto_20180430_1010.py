# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-30 09:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20180430_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='premium',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='agent',
            name='profile',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]
