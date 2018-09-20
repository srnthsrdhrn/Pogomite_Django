# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from users.models import User


class Service(models.Model):
    HOUR = 0
    DAY = 1
    MONTH = 2
    YEAR = 3
    SERVICE_TYPE = ((HOUR, "Hour"), (DAY, "Day"), (MONTH, "Month"), (YEAR, "Year"))
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, related_name='services')
    description = models.TextField(null=True, blank=True)
    type = models.IntegerField(choices=SERVICE_TYPE, default=HOUR)
    fare = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_created=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    worker = models.ForeignKey(User, related_name='worked_orders')
    service = models.ManyToManyField(Service, related_name='orders')
    customer = models.ForeignKey(User, related_name='requested_orders')
    startDateTime = models.DateTimeField(null=True, blank=True)
    endDateTime = models.DateTimeField(null=True, blank=True)
    no_of_slots = models.IntegerField(null=True, blank=True)
    worker_notified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Item(models.Model):
    name = models.CharField(max_length=500)
    order = models.ForeignKey(Order, related_name='items')
    description = models.TextField(null=True, blank=True)
    file = models.FileField(null=True, blank=True)
    amount = models.FloatField(null=True, blank=True)
    included = models.BooleanField(default=True)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now_add=True)
