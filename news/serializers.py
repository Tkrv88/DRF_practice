from rest_framework import serializers
from .models import *


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class ExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('name', 'color')


class NewsSerializerList(serializers.ModelSerializer):
    type = ExtraSerializer()

    class Meta:
        model = News
        fields = ('name', 'short_description', 'type')
