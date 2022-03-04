from django.urls import include, path
from rest_framework import routers
from rest_framework.routers import SimpleRouter

from .views import CommentsViewSet, ReviewsViewSet, UserViewSet, signup, token

router = SimpleRouter()

v1 = routers.DefaultRouter()
v1.register('users', UserViewSet, basename='users')

router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewsViewSet,
    basename='reviews'
)

router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentsViewSet,
    basename='reviews'
)

urlpatterns = [
    path('v1/', include(v1.urls)),
    path('v1/auth/signup/', signup, name='signup'),
    path('v1/auth/token/', token, name='token'),
    path('v1/', include(router.urls)),
]
