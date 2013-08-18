from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import GPSLogForm
import logging
import json


def insert_log(request):
    form = GPSLogForm(request.GET)
    logging.info(json.dumps(request.GET))
    if form.is_valid():
        form.save()
    else:
        return HttpResponse(json.dumps(form.errors), status=500)
    
    return HttpResponse('OK')

