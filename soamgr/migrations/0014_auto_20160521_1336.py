# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-21 05:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soamgr', '0013_auto_20160521_0209'),
    ]

    operations = [
        migrations.AddField(
            model_name='revieworderagreement',
            name='is_completed',
            field=models.BooleanField(default=False, verbose_name='Is Completed?'),
        ),
        migrations.AlterField(
            model_name='soa',
            name='status',
            field=models.CharField(choices=[('1', 'OA saved'), ('2', 'OA in-progress'), ('3', 'SOA in-progress'), ('4', 'SOA for review'), ('5', 'SOA finished')], default='1', max_length=1),
        ),
    ]