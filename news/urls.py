from django.urls import path, include
from rest_framework import routers

from .views import *

router_news = routers.SimpleRouter()
router_types = routers.SimpleRouter()

router_news.register(r'news', NewsViewSet)
# router_types.register(r'types', None)  # Дописать вьюху для типов и засунуть потом в паттерн

urlpatterns = [
    # path('api/v1/newslist/', NewsViewSet.as_view({"get": "list"})),
    # path('api/v1/newslist/<int:pk>/', NewsAPIUpdate.as_view()),
    # path('api/v1/newsdetail/<int:pk>/', NewsAPIDetailView.as_view()),
    path('api/v1/', include(router_news.urls)),

]
