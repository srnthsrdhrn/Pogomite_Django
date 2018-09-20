# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from users.models import Slider, User

admin.site.register(Slider)
admin.site.register(User)