from rest_framework import serializers

from .models import SportData, LegislativeDocument


# class SportDataSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = SportData
#         fields = "__all__"


class SportDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = SportData
        fields = (
        'id', 'title', 'attr', 'url', 'file', 'views', 'published_at', 'sport_type', 'author', 'publisher',
        'image', 'language')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['file'] = instance.get_file_url()
        representation['image'] = instance.get_image_url()
        representation['language'] = instance.get_language_display()
        return representation


class LegislativeDocumentSerializers(serializers.ModelSerializer):
    class Meta:
        model = LegislativeDocument
        fields = ('id', 'title', 'attr', 'url')
