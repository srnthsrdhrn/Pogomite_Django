# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-15 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=500)),
                ('description', models.TextField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to=b'')),
                ('amount', models.FloatField(blank=True, null=True)),
                ('included', models.BooleanField(default=True)),
                ('quantity', models.IntegerField(default=1)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('startDateTime', models.DateTimeField(blank=True, null=True)),
                ('endDateTime', models.DateTimeField(blank=True, null=True)),
                ('no_of_slots', models.IntegerField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('type', models.IntegerField(choices=[(0, 'Hour'), (1, 'Day'), (2, 'Month'), (3, 'Year')], default=0)),
                ('fare', models.FloatField(default=0)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]