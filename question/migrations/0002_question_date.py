# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default='2015-10-12'),
            preserve_default=False,
        ),
    ]
