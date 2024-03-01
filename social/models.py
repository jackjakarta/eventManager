from django.db import models
from django.contrib.auth import get_user_model
from website.models import MyModel, Event

AuthUser = get_user_model()


class Post(MyModel):
    class Meta:
        db_table = "user_posts"

    user = models.ForeignKey(AuthUser, null=False, on_delete=models.CASCADE)
    image = models.ImageField('Post Image', upload_to='user_posts/')
    description = models.TextField("Post Description", max_length=420, blank=True)
    event = models.ForeignKey(Event, null=True, blank=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(AuthUser, related_name="post_likes", blank=True)

    def __str__(self):
        return f"{self.user} - Post ID: {self.id}"

    def __repr__(self):
        return self.__str__()


class PostComment(MyModel):
    class Meta:
        db_table = "posts_comments"

    user = models.ForeignKey(AuthUser, null=False, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=False, on_delete=models.CASCADE)
    text = models.TextField("Comment", max_length=350, blank=True)

    def __str__(self):
        return f"{self.user} - Post ID: {self.post.id}"

    def __repr__(self):
        return self.__str__()
