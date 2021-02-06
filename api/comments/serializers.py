from rest_framework import serializers

from comments.models import Comment

from api.users.serializers import UserForCommentsSerializer


class CommentSerializer(serializers.ModelSerializer):

    user = UserForCommentsSerializer(allow_null=True)

    class Meta:
        model = Comment
        fields = '__all__'
