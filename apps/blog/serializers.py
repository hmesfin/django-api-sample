from rest_framework import serializers

from .models import Category
from .models import Comment
from .models import Post


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "url"]
        # extra_kwargs = {
        #     "url": {"view_name": "blog:category-detail", "lookup_field": "slug"},
        # }


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        # extra_kwargs = {
        #     "url": {"view_name": "blog:comment-detail"},
        # }


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ["slug"]
        # extra_kwargs = {
        #     "url": {"view_name": "blog:post-detail", "lookup_field": "slug"},
        # }
