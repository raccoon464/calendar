from my_calendar.models import Type, Bank, Status, Analytics, EventAnalytics, Event

def events():
    obj = Event.objects.all()
    data = []
    for i in obj:
        data += [{
            "pk": i.pk,
            "type": 0,
            "bank": 0,
            "event_analytics": 0,
            "status": 0,
            "title": i.title,
            "description": i.description,
            "details": i.details,
            "instruction": 0,
            "visible": 0,
            "start_datetime": i.start_datetime,
            "end_datetime": i.end_datetime,
            "last_update_datetime": i.last_update_datetime,
        }]

    return data