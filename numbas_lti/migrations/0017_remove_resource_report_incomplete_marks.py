# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 09:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('numbas_lti', '0016_auto_20160718_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='report_incomplete_marks',
        ),
    ]
