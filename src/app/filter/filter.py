from rest_framework import filters
from django.utils.translation import get_language


class SportDataFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        title = request.query_params.get('title', None)
        language = get_language()
        if title is None:
            return queryset
        if language == 'ru':
            queryset = queryset.filter(title_ru__icontains=title)
        elif language == 'en':
            queryset = queryset.filter(title_en__icontains=title)
        else:
            queryset = queryset.filter(title_uz__icontains=title)
        return queryset