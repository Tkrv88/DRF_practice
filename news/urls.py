from django.urls import path

from .views import NewsAPIView

urlpatterns = [
    path('api/v1/newslist/', NewsAPIView.as_view())
]