from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_api_key.permissions import HasAPIKey

from .models import Post, PostComment
from .serializers import PostSerializer, PostCommentSerializer


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [HasAPIKey | IsAuthenticatedOrReadOnly]
    authentication_classes = (JWTAuthentication, )


class PostCommentsViewSet(viewsets.ModelViewSet):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer
    permission_classes = [HasAPIKey | IsAuthenticated]
    authentication_classes = (JWTAuthentication, )
