# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyDataset',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('server_id', models.IntegerField(default=0)),
                ('application_id', models.IntegerField(default=0)),
                ('start_timestamp', models.IntegerField(default=0)),
            ],
        ),
    ]
