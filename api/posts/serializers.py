from rest_framework import serializers

from posts.models import Post, Category


class PostIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', ]


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'name', 'slug', 'title', 'image',
            'enabled', 'image_path', 'get_absolute_url',
            'click', 'like']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'image_menu', 'get_absolute_url']