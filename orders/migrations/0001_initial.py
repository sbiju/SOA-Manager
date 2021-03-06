# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-29 15:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('soamgr', '0019_progress_task_percent'),
        ('clientmgr', '0003_auto_20160529_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_name', models.CharField(blank=True, max_length=120, null=True, verbose_name='Partner Name')),
                ('due_date', models.DateField(blank=True, null=True)),
                ('smsf', models.CharField(blank=True, max_length=50, null=True, verbose_name='SMSF')),
                ('trust_fund', models.CharField(blank=True, max_length=50, null=True, verbose_name='Trust Fund')),
                ('company', models.CharField(blank=True, max_length=50, null=True, verbose_name='Company')),
                ('inside_super', models.CharField(blank=True, choices=[('NIL', 'NIL'), ('LOW', 'LOW'), ('MED', 'MED'), ('HIGH', 'HIGH')], max_length=50, null=True, verbose_name='Inside Super')),
                ('outside_super', models.CharField(blank=True, choices=[('NIL', 'NIL'), ('LOW', 'LOW'), ('MED', 'MED'), ('HIGH', 'HIGH')], max_length=50, null=True, verbose_name='Outside Super')),
                ('clientID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_order', to='clientmgr.Client')),
                ('s_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s_type', to='soamgr.SoaType')),
            ],
        ),
    ]
