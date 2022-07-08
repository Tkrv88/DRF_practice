from django.urls import path, include
from rest_framework import routers

from .views import *

router_news = routers.SimpleRouter()
router_types = routers.SimpleRouter()

router_news.register(r'news', NewsViewSet)
router_types.register(r'types', TypesViewSet)

urlpatterns = [
    path('api/v1/', include(router_news.urls)),
    path('api/v1/', include(router_types.urls)),

]
