# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Poem(models.Model):
    name = models.CharField(max_length=250, help_text="诗名")
    auth = models.CharField(max_length=100, help_text="作者")


class Student(models.Model):
    pass
