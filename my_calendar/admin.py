from django.contrib import admin

# Register your models here.
from my_calendar.models import Type, Bank, Status, Analytics, EventAnalytics, Event

admin.site.register(Type)
admin.site.register(Bank)
admin.site.register(Status)
admin.site.register(Analytics)
admin.site.register(EventAnalytics)
admin.site.register(Event)