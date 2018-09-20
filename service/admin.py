# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from service.models import Service, Item, Order

admin.site.register(Service)
admin.site.register(Item)
admin.site.register(Order)
