from rest_framework import serializers
from django.db.models import Sum

from .models import SportType

from app.models import SportData
from utils.models import State


class SportTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = SportType
        fields = ('id', 'title', 'attr', 'icon')

    def to_representation(self, instance):
        """Add count and file_views to representation"""
        representation = super().to_representation(instance)
        representation['count'] = SportData.objects.filter(sport_type=instance, state=State.objects.first()).count()
        representation['file_views'] = SportData.objects.filter(sport_type=instance, state=State.objects.first()).aggregate(
            views=Sum('views'))['views'] or 0
        return representation