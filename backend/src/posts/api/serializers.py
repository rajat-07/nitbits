from rest_framework import serializers
from ..models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'user', 'image', 'description')


class PostSerializerHiddenUser(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'description')


class PostSerializerCreate(serializers.ModelSerializer):
    content_image = serializers.ImageField()
    style_image = serializers.ImageField()

    class Meta:
        model = Post
        fields = ('title', 'description', 'content_image', 'style_image')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('user', 'post', 'comment')


class CommentSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('comment',)
