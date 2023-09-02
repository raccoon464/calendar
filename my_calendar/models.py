from django.db import models

# Create your models here.
from authentication.models import User
from common.models import BaseModel, BaseFileModel

class Type(BaseFileModel):
    name = models.CharField("name", null=True, max_length=100, blank=True)

class Bank(BaseFileModel):
    name = models.CharField("name", null=True, max_length=100, blank=True)
    color = models.CharField("color", null=True, max_length=100, blank=True)

class Status(models.Model):
    name = models.CharField("name", null=True, max_length=100, blank=True)

class Analytics(BaseFileModel):
    name = models.CharField("name", null=True, max_length=100, blank=True)
    url = models.CharField("url", null=True, max_length=100, blank=True)

class EventAnalytics(models.Model):
    analytics = models.ForeignKey(Analytics, on_delete=models.CASCADE, related_name="analytics")
    name = models.CharField("name", null=True, max_length=100, blank=True)
    url = models.CharField("url", null=True, max_length=100, blank=True)


class Event(BaseFileModel, ):
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name="type")
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name="bank")
    event_analytics = models.ForeignKey(EventAnalytics, on_delete=models.CASCADE, related_name="EventAnalytics")
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name="status")
    title = models.CharField("title", null=True, max_length=255, blank=True)
    description = models.TextField("description", null=True, blank=True)
    details = models.TextField("details", null=True, blank=True)
    instruction = models.TextField("instruction", null=True, blank=True)
    visible = models.CharField("visible", null=True, max_length=255, blank=True)
    start_datetime = models.DateTimeField("start_datetime", auto_now_add=True)
    end_datetime = models.DateTimeField("end_datetime", auto_now_add=True)
    last_update_datetime = models.DateTimeField("last_update_datetime", auto_now_add=True)