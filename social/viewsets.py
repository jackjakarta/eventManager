from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Post, PostComment
from .serializers import PostSerializer, PostCommentSerializer


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class PostCommentsViewSet(viewsets.ModelViewSet):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
