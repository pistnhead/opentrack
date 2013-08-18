from django.db import models

class Waypoint(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    timestamp = models.DateTimeField()
    hdop = models.CharField(max_length=255)
    altitude = models.FloatField()
    speed = models.FloatField()
    

