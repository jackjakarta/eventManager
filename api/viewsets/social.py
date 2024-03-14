from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers.social import PostSerializer, PostCommentSerializer
from social.models import Post, PostComment


@api_view(["GET"])
def get_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)

    return Response(serializer.data)


@api_view(["GET"])
def get_post_comments(request, post_id):
    post_comments = PostComment.objects.filter(post_id=post_id)
    serializer = PostCommentSerializer(post_comments, many=True)

    return Response(serializer.data)
