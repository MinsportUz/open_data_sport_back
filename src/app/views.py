from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend

from . import models
from . import serializers

from utils.pagination import TenPagination


def lockout_view(request):
    # You can add any context data here to pass to the template
    context = {
        'message': settings.HOST,
    }
    return render(request, 'lockout.html', context)


class SportDataView(viewsets.ModelViewSet):
    """The class is responsible for SportData CRUD functionality"""
    queryset = models.SportData.objects.all()
    serializer_class = serializers.SportDataSerializers
    http_method_names = ['get', ]
    pagination_class = TenPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('sport_type', 'created_at',)


class LegislativeDocumentView(viewsets.ModelViewSet):
    """The class is responsible for LegislativeDocument CRUD functionality"""
    queryset = models.LegislativeDocument.objects.all()
    serializer_class = serializers.LegislativeDocumentSerializers
    http_method_names = ['get', ]
    pagination_class = TenPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('created_at',)
