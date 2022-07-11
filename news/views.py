from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import *


class NewsViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get(self, request):
        n = News.objects.all()
        return Response({'news': NewsSerializerList(n, many=True).data})


class TypesViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

    @action(methods=['get'], detail=True)
    def news(self, request, pk=None):
        news = News.objects.filter(type_id=pk)
        return Response({'News for this type': [n.name for n in news]})
