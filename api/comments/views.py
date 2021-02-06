from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from posts.models import Post
from comments.models import Comment
from api.comments.serializers import CommentSerializer


class CommentsView(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):

    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(post=self.request.GET.get('post_id'))

    def perform_create(self, serializer):
        user = None
        if self.request.user.is_authenticated:
            user = self.request.user
        serializer.save(user=user)
