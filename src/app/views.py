from django.shortcuts import render
from rest_framework import viewsets
from django import http
from django.conf import settings
from . import models
from . import serializers


def lockout_view(request):
    # You can add any context data here to pass to the template
    context = {
        'message': settings.HOST,
    }
    return render(request, 'lockout.html', context)
