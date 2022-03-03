from django.urls import include, path
from rest_framework import routers

from api.views import CategoryViewSet, GenreViewSet, TitlesViewSet

router_v1 = routers.DefaultRouter()
router_v1.register('categories', CategoryViewSet, basename='categories')
router_v1.register('genres', GenreViewSet, basename='genres')
router_v1.register('titles', TitlesViewSet, basename='titles')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls.jwt'))
]
