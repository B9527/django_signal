# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-10 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='\u8bd7\u540d', max_length=250)),
                ('auth', models.CharField(help_text='\u4f5c\u8005', max_length=100)),
            ],
        ),
    ]
