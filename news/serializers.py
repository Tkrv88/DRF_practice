from rest_framework import serializers
from .models import *

class NewsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    short_description = serializers.CharField(max_length=255)
    full_description = serializers.CharField()
    type_id = serializers.IntegerField()