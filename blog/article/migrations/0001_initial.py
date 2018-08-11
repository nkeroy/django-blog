# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-19 04:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('main_body', models.CharField(max_length=200)),
                ('published_date', models.DateTimeField(verbose_name='Date Published')),
            ],
        ),
    ]
