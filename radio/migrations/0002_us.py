# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-31 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Us',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('valid', models.BooleanField(default=False)),
            ],
        ),
    ]