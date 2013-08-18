# -*- coding: utf-8 -*-
from django import forms
from .models import Waypoint

class GPSLogForm(forms.ModelForm):
    class Meta:
        model = Waypoint