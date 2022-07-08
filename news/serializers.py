from rest_framework import serializers
from .models import *


class NewsSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=50)
    # short_description = serializers.CharField(max_length=255)
    # full_description = serializers.CharField()
    # type_id = serializers.IntegerField()
    class Meta:
        model = News
        fields = "__all__"

    # def create(self, validated_data):
    #     return News.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get("name", instance.name)
    #     instance.short_description = validated_data.get("short_description", instance.short_description)
    #     instance.full_description = validated_data.get("full_description", instance.full_description)
    #     instance.type_id = validated_data.get("type_id", instance.type_id)
    #     instance.save()
    #     return instance
    #
    # def delete(self, instance, validated_data):
    #     return instance.delete()
