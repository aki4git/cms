# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Place(models.Model):
    name = models.CharField('清掃場所', max_length=255)
    users = models.ManyToManyField(User)

    def __unicode__(self):
        return self.name

class Task(models.Model):
    place = models.ForeignKey(Place, verbose_name='清掃場所', related_name='tasks')
    name = models.CharField('タスク名', max_length=255)
    user = models.ForeignKey(User, verbose_name='実施者')
    
    def __unicode__(self):
        return self.name

    