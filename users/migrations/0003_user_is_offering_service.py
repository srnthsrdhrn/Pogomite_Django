# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-06 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_mqtt_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_offering_service',
            field=models.BooleanField(default=False),
        ),
    ]
