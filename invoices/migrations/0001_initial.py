# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-18 15:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0003_auto_20161117_1631'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_issue', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('tax_rate', models.DecimalField(decimal_places=2, max_digits=4)),
                ('attachments', models.FileField(upload_to='uploads/')),
                ('name', models.CharField(max_length=500)),
                ('comment', models.CharField(max_length=500)),
                ('terms', models.CharField(max_length=5000)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.Client')),
                ('project', models.ManyToManyField(related_name='invoices', to='projects.Project')),
            ],
        ),
    ]