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
