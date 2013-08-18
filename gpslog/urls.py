from django.conf.urls import patterns, url

urlpatterns = patterns('gpslog.views',
        url(r'^$', 'insert_log', name='insert_log'),
)
