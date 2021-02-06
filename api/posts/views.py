from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny

from api.posts.serializers import CategorySerializer
from posts.models import Category


class CategoryApiView(mixins.ListModelMixin, viewsets.GenericViewSet):

    serializer_class = CategorySerializer

    def get_queryset(self):
        first_level = self.request.GET.get('first_level', None)
        if first_level:
            return Category.objects.filter(level=0)
        return Category.objects.all()

    def get_permissions(self):
        permission_classes = [AllowAny, ]
        return [permission() for permission in permission_classes]