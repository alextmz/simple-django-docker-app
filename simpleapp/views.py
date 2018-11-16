# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .models import string

def simpleapp(request):
    strings = string.objects.all()
    output = '<br>'.join([s.string for s in strings])
    return HttpResponse(output)
