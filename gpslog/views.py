from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def insert_log(request):
    return HttpResponse('Hello, world.')

