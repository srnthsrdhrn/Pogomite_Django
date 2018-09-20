# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    mobile_number = models.BigIntegerField(null=True, blank=True)
    is_offering_service = models.BooleanField(default=False)
    address = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True)
    wallet_address = models.CharField(max_length=1000)
    mqtt_token = models.CharField(max_length=512, unique=True, null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)


class Slider(models.Model):
    text = models.CharField(max_length=200)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)
