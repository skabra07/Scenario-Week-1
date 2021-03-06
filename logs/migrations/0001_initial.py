# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-10-30 16:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.TextField(verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='User'))),
                ('createdTime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('description', models.CharField(default='', max_length=5000)),
            ],
        ),
    ]
