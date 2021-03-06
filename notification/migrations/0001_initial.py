# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-29 15:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_unread', models.BooleanField(default=True)),
                ('subscribers_ids', models.TextField(default='', help_text="comma sepereted integer, read subscribers id's")),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='question.Question')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
