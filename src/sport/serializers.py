from rest_framework import serializers

from .models import SportType


class SportTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = SportType
        fields = ('id', 'title', 'attr', 'icon', 'state')