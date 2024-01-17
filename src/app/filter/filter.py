from rest_framework import filters
from django.utils.translation import get_language

from drf_yasg import openapi

from django.db.models import Q


class SportDataFilterBackend(filters.BaseFilterBackend):

    def get_schema_fields(self, view):
        return [
            coreapi.Field(
                name='sport_type',
                required=False,
                location='query',
                schema=coreschema.Integer(
                    title='sport_type',
                    description='sport_type',
                ),
            ),
            coreapi.Field(
                name='created_at',
                required=False,
                location='query',
                schema=coreschema.Integer(
                    title='created_at',
                    description='created_at',
                ),
            ),
        ]
    def filter_queryset(self, request, queryset, view):
        search = request.query_params.get('search', None)
        language = get_language()
        if search is None:
            return queryset
        if language == 'ru':
            queryset = queryset.filter(Q(title_ru__icontains=search) | Q(attr_ru__icontains=search) | Q(author__icontains=search))
        elif language == 'en':
            queryset = queryset.filter(Q(title_en__icontains=search) | Q(attr_en__icontains=search) | Q(author__icontains=search))
        else:
            queryset = queryset.filter(Q(title_uz__icontains=search) | Q(attr_uz__icontains=search) | Q(author__icontains=search))
        return queryset