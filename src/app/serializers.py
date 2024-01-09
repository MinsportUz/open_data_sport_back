from rest_framework import serializers

from .models import SportData


class SportDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = SportData
        fields = "__all__"