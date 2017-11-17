# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

from ..lr_app.models import Users
from models import Appointments
import datetime
from django.contrib import messages
from django import template
register = template.Library()

"""
Foreign Library: https://pypi.python.org/pypi/python-dateutil/2.6.1
"""
import dateutil
# Create your views here.
def default(request):
    """
    Route for rendering the default page for this app
    """
    Users.objects.updateAppointments(request.session['id'])
    context = {
        'user': Users.objects.get(id=request.session['id']),
        'date': datetime.datetime.now().strftime('%B %d, %Y'),
        'appointments': Users.objects.getAppointments(request.session['id'])
    }
    return render(request, 'appointments/default.html', context)

def add(request):
    """
    Route for processing the addition of a task to a user
    """
    if request.method == 'POST':
        response = Appointments.objects.addAppointment(request.POST, request.session['id'])
        if len(response) != 0:
            for message in response:
                messages.warning(request, message)
    return redirect('/appointments')

def delete_task(request, a_id):
    """
    Route for processing a task deletion
    """
    print Appointments.objects.delete_appointment(a_id)
    return redirect('/appointments')

def show_edit(request, a_id):
    """
    Route for rendering the edit page
    """
    return render(request, 'appointments/edit.html', {'appointment': Appointments.objects.get(id=a_id)})

def update(request, a_id):
    """
    Route for processing an update request
    """
    if request.method == 'POST':
        response = Appointments.objects.changeAppointment(request.POST, a_id)
        if len(response) != 0:
            for message in response:
                messages.warning(request, message)
            return redirect('/appointments/' + str(a_id) + '/edit')
    return redirect('/appointments')