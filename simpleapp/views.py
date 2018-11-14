# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def simpleapp(request):
    return HttpResponse("Hello, world.")
