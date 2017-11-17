# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.
def default(request):
    """
    Route for rendering the default page for this app
    """
    return HttpResponse('default page')