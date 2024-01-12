from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Sum
from drf_yasg.utils import swagger_auto_schema

from . import models
from . import serializers
from .filter.filter import SportDataFilterBackend
from .params import params

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
    queryset = models.SportData.objects.filter(state=State.objects.first())
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
    queryset = models.LegislativeDocument.objects.filter(state=State.objects.first())
    serializer_class = serializers.LegislativeDocumentSerializers
    http_method_names = ['get', ]
    pagination_class = TenPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('created_at',)


class DataFilterView(viewsets.ModelViewSet):
    """The class is responsible for SportData CRUD functionality"""
    queryset = models.SportData.objects.filter(state=State.objects.first())
    serializer_class = serializers.SportDataSerializers
    http_method_names = ['get', ]
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('sport_type', 'created_at',)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        document_count = queryset.count()
        legislative_count = models.LegislativeDocument.objects.all().count()
        total_views = queryset.aggregate(total_views=Sum('views'))['total_views']
        youtube_data = serializers.YoutubeViewsSerializers(queryset, many=True).data
        youtube_views = sum([i['youtube_views'] for i in youtube_data])
        sport_type_count = SportType.objects.filter(state=State.objects.first()).count()
        return Response({
            'document_count': document_count,
            'legislative_count': legislative_count,
            'files_views': total_views,
            'youtube_views': youtube_views,
            'total_views': total_views + youtube_views,
            'sport_type_count': sport_type_count,
        }, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class SearchDataView(viewsets.ModelViewSet):
    """The class is responsible for SportData CRUD functionality"""
    queryset = models.SportData.objects.filter(state=State.objects.first())
    serializer_class = serializers.SportDataSerializers
    http_method_names = ['get', ]
    pagination_class = TenPagination
    filter_backends = (SportDataFilterBackend,)
    filterset_fields = ('author', 'title',)

    @swagger_auto_schema(manual_parameters=params, responses={200: 'OK'},
                         operation_id='filter by author and title')
    def list(self, request, *args, **kwargs):
        return super(SearchDataView, self).list(request, *args, **kwargs)


class GetDataFilterByviewsView(viewsets.ModelViewSet):
    """The class is responsible for SportData CRUD functionality"""
    queryset = models.SportData.objects.filter(state=State.objects.first()).order_by('-views')
    serializer_class = serializers.SportDataSerializers
    http_method_names = ['get', ]
    pagination_class = TenPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('sport_type',)

    def list(self, request, *args, **kwargs):
        sort = request.query_params.get('sort', None)
        if sort == 'youtube':
            queryset = self.filter_queryset(self.get_queryset())
            youtube_data = serializers.SportDataSerializers(queryset, many=True).data
            youtube_data = sorted(youtube_data, key=lambda x: x['youtube_views'], reverse=True)
            page = self.paginate_queryset(youtube_data)
            if page is not None:
                return self.get_paginated_response(page)
        else:
            return super(GetDataFilterByviewsView, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.increase_views()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class AboutView(viewsets.ModelViewSet):
    """The class is responsible for About CRUD functionality"""
    queryset = models.About.objects.filter(state=State.objects.first())
    serializer_class = serializers.AboutSerializers
    http_method_names = ['get', ]

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class FooterView(viewsets.ModelViewSet):
    """The class is responsible for Footer CRUD functionality"""
    queryset = models.Footer.objects.filter(state=State.objects.first())
    serializer_class = serializers.FooterSerializers
    http_method_names = ['get', ]

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class GetDataView(viewsets.ModelViewSet):
    """The class is responsible for SportData Get only id functionality"""
    queryset = models.SportData.objects.filter(state=State.objects.first())
    serializer_class = serializers.SportDataSerializers
    http_method_names = ['get', ]

    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)