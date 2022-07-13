from rest_framework import serializers
from .models import *


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ("name", "color")


class NewsSerializer(serializers.ModelSerializer):
    type = TypeSerializer()

    class Meta:
        model = News
        fields = ("name", "short_description", "type")
