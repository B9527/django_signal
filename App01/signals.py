#!/usr/bin/python
# coding:utf-8

"""
项目名：SingalDemo - the name of the current project.
文件名：singal - the name of the new file which you specify in the New File dialog box during the file creation.
电脑：Administrator - baiyang
时间：2018/6/10 23:17 
IDE:PyCharm - the name of the IDE in which the file will be created.
"""

from django.dispatch import Signal, receiver
from django.db.models.signals import post_save, pre_save
from .models import Student

signal_bai = Signal(providing_args="bai")


@receiver(signal_bai)
def signal_callback(sender, **kwargs):
    print(sender, sender, kwargs)
    print(signal_callback)


@receiver(post_save, sender=Student)
def pre_save_callback(sender, **kwargs):
    print(sender, kwargs)
    print("pre_save_callback")
