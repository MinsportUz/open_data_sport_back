from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Sum
from rest_framework.decorators import action

from . import models
from . import serializers

from utils.pagination import TenPagination
from utils.models import State

from sport.models import SportType


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
    filterset_fields = ('sport_type',)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.increase_views()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class LegislativeDocumentView(viewsets.ModelViewSet):
    """The class is responsible for LegislativeDocument CRUD functionality"""
    queryset = models.LegislativeDocument.objects.all()
    serializer_class = serializers.LegislativeDocumentSerializers
    http_method_names = ['get', ]
    pagination_class = TenPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('created_at',)


class DataFilterView(viewsets.ModelViewSet):
    """The class is responsible for SportData CRUD functionality"""
    queryset = models.SportData.objects.all()
    serializer_class = serializers.SportDataSerializers
    http_method_names = ['get', ]
    # pagination_class = TenPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('sport_type', 'created_at',)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        document_count = queryset.count()
        legislative_count = models.LegislativeDocument.objects.all().count()
        total_views = queryset.aggregate(total_views=Sum('views'))['total_views']
        sport_type_count = SportType.objects.filter(state=State.objects.first()).count()
        return Response({
            'document_count': document_count,
            'legislative_count': legislative_count,
            'total_views': total_views,
            'sport_type_count': sport_type_count,
        }, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
