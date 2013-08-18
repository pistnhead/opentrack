from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import GPSLogForm
import logging
import json


def insert_log(request):
    form = GPSLogForm(request.GET)
    if form.is_valid():
        form.save()
    else:
        logging.errror(json.dumps(request.GET))
        return HttpResponse('Yikes', status=500)
    
    return HttpResponse('OK')

