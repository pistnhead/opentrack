from django.contrib import admin
from .models import Waypoint

class WaypointAdmin(admin.ModelAdmin):
    class Meta:
        model = Waypoint
admin.site.register(Waypoint, WaypointAdmin)
