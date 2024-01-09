from django.db import models
from django.contrib.auth import get_user_model

AuthUser = get_user_model()


class MyModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Venue(MyModel):
    class Meta:
        db_table = "venues"

    name = models.CharField("Venue Name", max_length=120, unique=True, null=False)
    address = models.CharField("Venue Address", max_length=250)
    city = models.CharField("Venue City", max_length=120, null=True)
    zip_code = models.CharField("Zip Code", max_length=20)
    website = models.URLField("Venue Website")
    email = models.EmailField("Venue Email")
    manager = models.ForeignKey(AuthUser, blank=True, null=True, on_delete=models.SET_NULL)
    image = models.ImageField("Venue Image", upload_to="venue_images/", default=None)

    def __str__(self):
        return self.name


class Promoter(MyModel):
    class Meta:
        db_table = "promoters"

    name = models.CharField("Promoter", max_length=120, unique=True, null=False)
    city = models.CharField("Promoter Location", max_length=120, blank=True)
    email = models.EmailField("Promoter Email", max_length=250)
    website = models.URLField("Promoter Website", blank=True)
    manager = models.ForeignKey(AuthUser, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Event(MyModel):
    class Meta:
        db_table = "events"

    name = models.CharField("Event Name", max_length=250, unique=True, null=False)
    event_date = models.DateTimeField("Event Date")
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    promoter = models.ForeignKey(Promoter, blank=True, null=True, on_delete=models.CASCADE)
    manager = models.ForeignKey(AuthUser, null=True, on_delete=models.SET_NULL)
    event_flyer = models.ImageField("Event Flyer", upload_to='event_flyers/', default=None, null=True)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(AuthUser, related_name='attended_events', blank=True)

    def __str__(self):
        return self.name


class Profile(MyModel):
    class Meta:
        db_table = "user_profiles"

    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatars/", default=None, blank=True)

    def __str__(self):
        return str(self.user)


class NewsletterSub(MyModel):
    class Meta:
        db_table = "newsletter_subs"

    email = models.EmailField(unique=True, null=False)

    def __str__(self):
        return self.email
