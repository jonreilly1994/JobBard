# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-11 02:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_auto_20170410_2038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='zip_code',
        ),
    ]
