# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-19 19:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tempmgr', '0002_auto_20160520_0032'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FormattingDetails',
            new_name='FormattingDetail',
        ),
        migrations.RenameModel(
            old_name='Subtemplates',
            new_name='Subtemplate',
        ),
    ]
