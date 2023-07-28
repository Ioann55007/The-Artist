from rest_framework import serializers

from .models import Picture




class PictureCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ['name', 'slug', 'category', 'author', 'description']
