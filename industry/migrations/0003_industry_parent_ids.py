# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-12 12:45
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('industry', '0002_auto_20180212_0114'),
    ]

    operations = [
        migrations.AddField(
            model_name='industry',
            name='parent_ids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.BigIntegerField(), default=[0], size=None),
            preserve_default=False,
        ),
    ]
