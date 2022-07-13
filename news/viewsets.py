from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import *


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    # type_name = Type.objects.values_list('name', flat=True).distinct()
    serializer_class = NewsSerializer


class TypesViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

    @action(methods=['get'], detail=True)
    def news(self, request, pk=None):
        news = News.objects.filter(type_id=pk)
        return Response({'News for this type': [n.name for n in news]})
