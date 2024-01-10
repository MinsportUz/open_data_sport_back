from rest_framework import serializers

from .models import SportData, LegislativeDocument


# class SportDataSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = SportData
#         fields = "__all__"


class SportDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = SportData
        fields = ('id', 'title', 'attr', 'url', 'file', 'views', 'published_at', 'state', 'sport_type')
        # depth = 1


class LegislativeDocumentSerializers(serializers.ModelSerializer):
    class Meta:
        model = LegislativeDocument
        fields = ('id', 'title', 'attr', 'url', 'state')