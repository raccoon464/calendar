from django.urls import path
from my_calendar.api.views import index, EventsView

urlpatterns = [
    path('', index, name='index'),
    path('events/', EventsView.as_view()),

]