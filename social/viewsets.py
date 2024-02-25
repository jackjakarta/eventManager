from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework_simplejwt.authentication import JWTAuthentication

from users.utils.apikey_auth import UserHasAPIKey
from .models import Post, PostComment
from .serializers import PostSerializer, PostCommentSerializer


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [HasAPIKey | UserHasAPIKey | IsAuthenticated]
    authentication_classes = (JWTAuthentication, )


class PostCommentsViewSet(viewsets.ModelViewSet):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer
    permission_classes = [HasAPIKey | UserHasAPIKey | IsAuthenticated]
    authentication_classes = (JWTAuthentication, )
