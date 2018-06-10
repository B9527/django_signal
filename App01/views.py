# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from django.views import View
from .models import Poem
from .signals import signal_bai
from django.db.models.signals import post_save, pre_save


# Create your views here.

class HelloView(View):
    def get(self, request):
        signal_bai.send(sender=None, bai="test")
        poem = Poem.objects.all()
        return render(request, 'htmls/hello.html',{"poem":poem})


class AddUser(View):
    def get(self, request):

        poem = Poem()
        poem.name = "静夜思"
        poem.auth = "bai yang"
        poem.save()
        return render(request, 'htmls/hello.html')

