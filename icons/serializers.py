from rest_framework import serializers

from icons.models import Icon


class IconDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Icon
        fields = ['name', 'slug', 'category', 'author', 'description']


class IconCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Icon
        fields = ['name', 'slug', 'category', 'author', 'description']
