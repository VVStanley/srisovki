from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from api.posts.serializers import PostSerializer, PostIdSerializer
from posts.models import Post


class WhatColorizeApiView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self, request):
        '''Возвращаем id постов в категории'''
        queryset = []
        act_category = request.GET.get('act_category', None)
        if act_category:
            id_cat = act_category[:-1].split(',')
            queryset = Post.objects.filter(enabled=True, categories__in=id_cat, user__is_superuser=True)
        else:
            queryset = Post.objects.filter(enabled=True, user__is_superuser=True)
        serializer = PostIdSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_permissions(self):
        permission_classes = [AllowAny, ]
        return [permission() for permission in permission_classes]