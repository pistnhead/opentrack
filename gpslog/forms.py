# -*- coding: utf-8 -*-
from django import forms
from .models import Waypoint
from datetime import datetime


class DateTimeMicroseconds(forms.DateTimeField):
    def clean(self, value):
        value = str(datetime.fromtimestamp(int(value)/1000))
        return value
    

class GPSLogForm(forms.ModelForm):
    timestamp = DateTimeMicroseconds()
    class Meta:
        model = Waypoint
