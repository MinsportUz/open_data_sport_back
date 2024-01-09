from rest_framework import viewsets, status
from rest_framework.response import Response
from . import models
from . import serializers


class StateView(viewsets.ModelViewSet):
    """The class is responsible for State CRUD functionality"""
    queryset = models.State.objects.all()
    serializer_class = serializers.StateSerializer
    http_method_names = ['get']

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)