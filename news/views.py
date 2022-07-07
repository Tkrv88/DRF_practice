from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import NewsSerializer


class NewsAPIView(APIView):
    # queryset = News.objects.all()
    # serializer_class = NewsSerializer
    def get(self, request):
        new = News.objects.all()
        return Response({'posts': NewsSerializer(new, many=True).data})

    def post(self, request):
        post_new = News.objects.create(
            name=request.data['name'],
            short_description=request.data['short_description'],
            full_description=request.data['full_description'],
            type_id=request.data['type_id']
        )
        return Response({'post': NewsSerializer(post_new).data})