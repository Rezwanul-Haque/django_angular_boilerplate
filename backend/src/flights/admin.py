from django.contrib import admin
# models
from flights.models import Schedule


#Custom action command
def oneway_trip(modeladmin, request, queryset):
    queryset.update(trip_type='One Way')

oneway_trip.short_description = "Set Trip type to One Way"


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['flight_no', 'airline', 'trip_type']
    ordering = ['airline',]
    actions = [oneway_trip]

# Register your models here.
admin.site.register(Schedule, ScheduleAdmin)