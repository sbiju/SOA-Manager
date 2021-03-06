# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-21 06:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soamgr', '0015_auto_20160521_1403'),
    ]

    operations = [
        migrations.RenameField(
            model_name='soa',
            old_name='is_claim',
            new_name='is_claimed',
        ),
        migrations.RenameField(
            model_name='soa',
            old_name='is_complete',
            new_name='is_completed',
        ),
        migrations.RenameField(
            model_name='soa',
            old_name='is_submit',
            new_name='is_submitted',
        ),
        migrations.AddField(
            model_name='soa',
            name='is_approved',
            field=models.BooleanField(default=False, verbose_name='Is completed?'),
        ),
    ]
