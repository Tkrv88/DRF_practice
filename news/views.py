from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import *


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    @action(methods=['get'], detail=False)
    def type(self, request):
        types = Type.objects.all()
        return Response({'type': [t.name for t in types]})


class TypesViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

    @action(methods=['get'], detail=True)
    def news(self, request, pk=None):
        news = News.objects.filter(type_id=pk)
        return Response({'News for this type': [n.name for n in news]})
