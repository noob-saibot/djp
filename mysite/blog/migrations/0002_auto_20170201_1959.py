# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WikiInform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('post_id', models.CharField(max_length=255)),
                ('datetime', models.DateTimeField(verbose_name='Date')),
                ('content', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='WikiInfo',
        ),
    ]
