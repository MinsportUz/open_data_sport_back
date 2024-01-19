from rest_framework import serializers

from .models import SportData, LegislativeDocument, About, Footer
from .youtube import youtube_video_stats


class SportDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = SportData
        fields = (
            'id', 'title', 'attr', 'url', 'file', 'views', 'published_at', 'sport_type', 'author', 'publisher', 'uuid',
            'image', 'language')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['file'] = instance.get_file_url()
        representation['image'] = instance.get_image_url()
        representation['language'] = instance.get_language_display()
        representation['youtube_views'] = youtube_video_stats(instance.url)
        return representation


class LegislativeDocumentSerializers(serializers.ModelSerializer):
    class Meta:
        model = LegislativeDocument
        fields = ('id', 'title', 'attr', 'url')


class YoutubeViewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = SportData
        fields = ('url', 'views')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['youtube_views'] = youtube_video_stats(instance.url)
        return representation


class AboutSerializers(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('id', 'title', 'content', 'image', 'state')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = instance.get_image_url()
        return representation


class FooterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = '__all__'