# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-23 17:34
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soamgr', '0017_auto_20160521_2227'),
    ]

    operations = [
        migrations.CreateModel(
            name='EvalItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eval_name', models.CharField(max_length=254, verbose_name='Progress Name')),
                ('description', models.CharField(blank=True, max_length=254, null=True, verbose_name='Description')),
                ('question', models.CharField(blank=True, max_length=254, null=True, verbose_name='Question')),
                ('parent', models.CharField(max_length=254, verbose_name='Parent Item')),
                ('sort', models.SmallIntegerField()),
            ],
            options={
                'verbose_name': 'Evaluation Item',
                'verbose_name_plural': 'Evaluation Items',
            },
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prog_name', models.CharField(max_length=254, verbose_name='Progress Name')),
                ('description', models.CharField(blank=True, max_length=254, null=True, verbose_name='Description')),
                ('question', models.CharField(blank=True, max_length=254, null=True, verbose_name='Question')),
                ('parent', models.CharField(max_length=254, verbose_name='Parent Item')),
                ('sort', models.SmallIntegerField()),
            ],
            options={
                'verbose_name': 'Task Progress',
                'verbose_name_plural': 'Task Progress Items',
            },
        ),
        migrations.AddField(
            model_name='soa',
            name='eval_items',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='soa',
            name='progress_items',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='goal',
            name='parent',
            field=models.CharField(max_length=254, verbose_name='Parent Goal'),
        ),
    ]
