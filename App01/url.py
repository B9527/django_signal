#!/usr/bin/python
# coding:utf-8

"""
项目名：SingalDemo - the name of the current project.
文件名：url - the name of the new file which you specify in the New File dialog box during the file creation.
电脑：Administrator - baiyang
时间：2018/6/10 22:29 
IDE:PyCharm - the name of the IDE in which the file will be created.
"""

from django.conf.urls import url
from .views import HelloView, AddUser

urlpatterns = [
    url(r'^hello/$', HelloView.as_view(), name="hello"),
    url(r'^add_user/$', AddUser.as_view(), name="add_user")
]
