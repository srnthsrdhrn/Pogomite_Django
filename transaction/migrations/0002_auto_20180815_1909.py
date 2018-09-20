# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-15 13:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service', '0002_auto_20180815_1909'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_transactions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='transaction',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_transactions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='paymentrequest',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='service.Order'),
        ),
        migrations.AddField(
            model_name='paymentrequest',
            name='payee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_payments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='paymentrequest',
            name='transaction',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='transaction.Transaction'),
        ),
        migrations.AddField(
            model_name='paymentrequest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requested_payments', to=settings.AUTH_USER_MODEL),
        ),
    ]
