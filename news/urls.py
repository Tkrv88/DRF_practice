from django.urls import path, include
from rest_framework import routers

from .views import *

router_news = routers.SimpleRouter()
router_types = routers.SimpleRouter()

router_news.register(r'news', NewsViewSet)
router_types.register(r'types', TypesViewSet)

urlpatterns = [
    path('', include(router_news.urls)),
    path('', include(router_types.urls)),

]
