from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from datetime import datetime, timezone
from . import layout


def size(data):
    arr_json = {"content": data}
    b = len( ""+ str(arr_json) + "" )
    return b

def index(request):
    return HttpResponse("CRYPTON LLC")

class EventsView(APIView):
    def get(self, request):
        data = layout.events()
        return Response(data, headers={"x-tools-length": size(data), "Access-Control-Expose-Headers":"x-tools-length"})