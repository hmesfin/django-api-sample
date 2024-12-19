from rest_framework.viewsets import ModelViewSet

from .models import Category
from .models import Comment
from .models import Post
from .serializers import CategorySerializer
from .serializers import CommentSerializer
from .serializers import PostSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
