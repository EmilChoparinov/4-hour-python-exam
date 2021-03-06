# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 17:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lr_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='appointments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.TextField()),
                ('status', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='lr_app.Users')),
            ],
        ),
    ]
