from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    # @action(methods=['get'], detail=False)
    # def type(self, request):
    #     tips = Type.objects.all()
    #     return Response({'tips': [t.name for t in tips]})

    @action(methods=['get'], detail=False)
    def type(self, request):
        types = Type.objects.all()
        return Response({'type': [t.name for t in types]})

# class NewsAPIList(generics.ListCreateAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer
#
#
# class NewsAPIUpdate(generics.UpdateAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer
#
#
# class NewsAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer
#
#
# class NewsAPIView(APIView):
#     # queryset = News.objects.all()
#     # serializer_class = NewsSerializer
#     def get(self, request):
#         new = News.objects.all()
#         return Response({'posts': NewsSerializer(new, many=True).data})
#
#     def post(self, request):
#         serializer = NewsSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({"post": serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = News.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
#
#         serializer = NewsSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#
#         try:
#             instance = News.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
#
#         serializer = NewsSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({"post": "Post " + str(pk) + " deleted"})
