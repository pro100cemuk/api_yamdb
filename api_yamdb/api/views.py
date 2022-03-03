from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters, mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination

from reviews.models import Category, Genre, Titles

from .permissions import IsRoleAdmin, ReadOnly
from .serializers import CategorySerializer, GenreSerializer, TitlesSerializer


class ListCreateDestroyViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    pass


class CategoryViewSet(ListCreateDestroyViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsRoleAdmin,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^name',)
    pagination_class = LimitOffsetPagination

    def get_permissions(self):
        if self.action == 'list':
            return (ReadOnly(),)
        return super().get_permissions()


class GenreViewSet(ListCreateDestroyViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsRoleAdmin,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^name',)
    pagination_class = LimitOffsetPagination

    def get_permissions(self):
        if self.action == 'list':
            return (ReadOnly(),)
        return super().get_permissions()


class TitlesViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer
    permission_classes = (IsRoleAdmin,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('category', 'genre', 'name', 'year')
    pagination_class = LimitOffsetPagination

    def get_permissions(self):
        if (
            self.action == 'retrieve'
            or self.action == 'list'
        ):
            return (ReadOnly(),)
        return super().get_permissions()
