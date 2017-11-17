# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..lr_app.models import Users

from django.db import models

import datetime

class AppointmentsManager(models.Manager):
    """
    Manages the incomming requests from the server to process them into the database
    """
    def addAppointment(self, data, u_id):
        """
        Adds an appointment to the user
        """
        response = []
        print str(datetime.datetime.time(datetime.datetime.now()))[:5]
        print data['time']
        print data['time'] < str(datetime.datetime.time(datetime.datetime.now()))[:5]
        if not data['date']:
            response.append('Date field cannot be left empty')
        elif data['date'] < str(datetime.date.today()):
            response.append('Date has already passed')
        if not data['time']:
            response.append('Time field cannot be left empty')
        elif data['time'] < str(datetime.datetime.time(datetime.datetime.now()))[:5] and data['date'] == str(datetime.date.today()):
            response.append('Time has already passed')
        if not data['task']:
            response.append('Tasks cannot be left empty')

        if len(response) == 0:
            Appointments.objects.create(
                task = data['task'],
                status = "pending",
                date = data['date'],
                time = data['time'],
                user = Users.objects.get(id=u_id)
            )
        return response

    def delete_appointment(self, a_id):
        """
        Deletes an existing appointment from the database
        """
        response = []
        if len(Appointments.objects.filter(id=a_id)) == 0:
            response.append('Appointment does not exist!')
        if len(response) == 0:
            Appointments.objects.get(id=a_id).delete()
        return response

    def changeAppointment(self, data, a_id):
        """
        Changes an appointment
        """
        response = []
        if not data['date']:
            response.append('Date field cannot be left empty')
        elif data['date'] < str(datetime.date.today()):
            response.append('Date has already passed')
        # elif data['time'] < str(datetime.datetime.time(datetime.datetime.now())):
        #     response.append('Time has already passed')

        if not data['time']:
            response.append('Time field cannot be left empty')

        if not data['task']:
            response.append('Tasks cannot be left empty')

        if len(response) == 0:
            a = Appointments.objects.get(id=a_id)
            a.task = data['task']
            a.status = data['status']
            a.date = data['date']
            a.time = data['time']
            a.save()
        return response

# Create your models here.
class Appointments(models.Model):
    task = models.TextField()
    status = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    user = models.ForeignKey(Users, related_name='appointments')
    objects = AppointmentsManager()