from rest_framework import viewsets, status
from rest_framework.response import Response

from . import models
from . import serializers

from utils.pagination import TenPagination


class SportTypeView(viewsets.ModelViewSet):
    """The class is responsible for SportType CRUD functionality"""
    queryset = models.SportType.objects.all()
    serializer_class = serializers.SportTypeSerializers
    http_method_names = ['get']
    pagination_class = TenPagination

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
