# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-18 09:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientID', models.CharField(max_length=254, verbose_name='Client Name')),
                ('xplanID', models.CharField(max_length=20, verbose_name='XPLAN ID')),
                ('title', models.CharField(blank=True, max_length=20, null=True, verbose_name='Title')),
                ('lastName', models.CharField(max_length=50, verbose_name='Last Name')),
                ('middleName', models.CharField(blank=True, max_length=50, null=True, verbose_name='Middle Name')),
                ('firstName', models.CharField(max_length=50, verbose_name='First Name')),
                ('secondName', models.CharField(blank=True, max_length=50, null=True, verbose_name='Second Name')),
                ('preferredName', models.CharField(blank=True, max_length=50, null=True, verbose_name='Preferred Name')),
                ('fullName', models.CharField(max_length=254, verbose_name='Full Name')),
                ('completeName', models.CharField(max_length=254, verbose_name='Complete Name')),
                ('photo', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Photo')),
                ('email', models.EmailField(max_length=50, verbose_name='Email Address')),
                ('mobilePhone', models.CharField(max_length=50, verbose_name='Mobile Phone')),
                ('homePhone', models.CharField(max_length=50, verbose_name='Home Phone')),
                ('addressLine1', models.CharField(max_length=255, verbose_name='Address Line 1')),
                ('addressLine2', models.CharField(max_length=255, verbose_name='Address Line 2')),
                ('addressLine3', models.CharField(max_length=255, verbose_name='Address Line 3')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True, verbose_name='Gender')),
                ('birthDate', models.DateField(verbose_name='Birth Date')),
                ('deathDate', models.DateField(verbose_name='Death Date')),
                ('maritalStatus', models.CharField(blank=True, choices=[('S', 'Single'), ('M', 'Maried'), ('D', 'Divorced'), ('W', 'Widower')], max_length=1, null=True, verbose_name='Marital Status')),
                ('religion', models.CharField(max_length=50, verbose_name='Religion')),
                ('occupation', models.CharField(blank=True, max_length=50, null=True, verbose_name='Title')),
                ('income', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Income')),
                ('health', models.CharField(blank=True, max_length=254, null=True, verbose_name='Health Condition')),
                ('isSmoker', models.BooleanField(default=False, verbose_name='Is Smoker?')),
                ('willExists', models.BooleanField(default=False, verbose_name='Will Exists?')),
                ('powerOfAttorney', models.CharField(blank=True, max_length=254, null=True, verbose_name='Health Condition')),
                ('DefaultTemplate', models.CharField(blank=True, max_length=254, null=True, verbose_name='Default Template')),
                ('DefaultFormatting', models.CharField(blank=True, max_length=254, null=True, verbose_name='Default Formatting')),
                ('DefaultStrategies', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Default Strategies')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('entityID', models.CharField(max_length=254, verbose_name='Client Name')),
                ('xplanID', models.CharField(max_length=20, verbose_name='XPLAN ID')),
                ('name', models.CharField(max_length=255, verbose_name='Entity Name')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Entity Description')),
                ('entType', models.CharField(choices=[('SMSF', 'Self-Managed Super Fund'), ('TF', 'Trust Fund'), ('C', 'Company')], max_length=255, verbose_name='Entity Type')),
                ('incomes', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Income')),
                ('expenses', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Expense')),
                ('investments', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Investments')),
                ('assets', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Assets')),
                ('debts', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Debts')),
                ('netFinancial', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Net Financial Position')),
                ('defensiveAssets', models.FloatField(verbose_name='Defensive Assets')),
                ('growthAssets', models.FloatField(verbose_name='Growth Assets')),
                ('riskProfile', models.CharField(max_length=100, verbose_name='Risk Profile')),
                ('assessment', models.CharField(max_length=100, verbose_name='Assessment')),
                ('about', models.CharField(max_length=255, verbose_name='About')),
            ],
            options={
                'verbose_name': 'Entity',
                'verbose_name_plural': 'Entities',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('partnerID', models.CharField(max_length=254, verbose_name='Client Name')),
                ('xplanID', models.CharField(max_length=20, verbose_name='XPLAN ID')),
                ('title', models.CharField(blank=True, max_length=20, null=True, verbose_name='Title')),
                ('lastName', models.CharField(max_length=50, verbose_name='Last Name')),
                ('middleName', models.CharField(blank=True, max_length=50, null=True, verbose_name='Middle Name')),
                ('firstName', models.CharField(max_length=50, verbose_name='First Name')),
                ('secondName', models.CharField(blank=True, max_length=50, null=True, verbose_name='Second Name')),
                ('preferredName', models.CharField(blank=True, max_length=50, null=True, verbose_name='Preferred Name')),
                ('fullName', models.CharField(max_length=254, verbose_name='Full Name')),
                ('completeName', models.CharField(max_length=254, verbose_name='Complete Name')),
                ('photo', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Photo')),
                ('email', models.EmailField(max_length=50, verbose_name='Email Address')),
                ('mobilePhone', models.CharField(max_length=50, verbose_name='Mobile Phone')),
                ('homePhone', models.CharField(max_length=50, verbose_name='Home Phone')),
                ('addressLine1', models.CharField(max_length=255, verbose_name='Address Line 1')),
                ('addressLine2', models.CharField(max_length=255, verbose_name='Address Line 2')),
                ('addressLine3', models.CharField(max_length=255, verbose_name='Address Line 3')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True, verbose_name='Gender')),
                ('birthDate', models.DateField(verbose_name='Birth Date')),
                ('deathDate', models.DateField(verbose_name='Death Date')),
                ('maritalStatus', models.CharField(blank=True, choices=[('S', 'Single'), ('M', 'Maried'), ('D', 'Divorced'), ('W', 'Widower')], max_length=1, null=True, verbose_name='Marital Status')),
                ('religion', models.CharField(max_length=50, verbose_name='Religion')),
                ('occupation', models.CharField(blank=True, max_length=50, null=True, verbose_name='Title')),
                ('income', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Income')),
                ('health', models.CharField(blank=True, max_length=254, null=True, verbose_name='Health Condition')),
                ('isSmoker', models.BooleanField(default=False, verbose_name='Is Smoker?')),
                ('willExists', models.BooleanField(default=False, verbose_name='Will Exists?')),
                ('powerOfAttorney', models.CharField(blank=True, max_length=254, null=True, verbose_name='Health Condition')),
                ('DefaultTemplate', models.CharField(blank=True, max_length=254, null=True, verbose_name='Default Template')),
                ('DefaultFormatting', models.CharField(blank=True, max_length=254, null=True, verbose_name='Default Formatting')),
                ('DefaultStrategies', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Default Strategies')),
            ],
            options={
                'verbose_name': 'Partner',
                'verbose_name_plural': 'Partners',
            },
        ),
    ]
