# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-18 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('summary', models.CharField(default='', max_length=500)),
                ('isbn', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=500)),
                ('source', models.CharField(max_length=500)),
                ('points', models.IntegerField(null=True)),
                ('author', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
