from django import forms
from django.contrib.auth import get_user_model

from .models import Promoter, Venue, Event, Profile, Artist

AuthUser = get_user_model()


class SignUpForm(forms.ModelForm):
    class Meta:
        model = AuthUser
        fields = ("email", "first_name", "last_name", )
        labels = {
            "email": "",
            "first_name": "",
            "last_name": "",
        }
        widgets = {
            "email": forms.TextInput(attrs={"class": "form-control", "placeholder": "Email Address"}),
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Last Name"}),
        }


class AddArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ("name", "bio", "image", "email", "website", "city", "country", )
        labels = {
            "name": "",
            "bio": "",
            "email": "",
            "website": "",
            "city": "",
            "country": "",
            "image": "Artist Image:"
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Artist/Band Name"}),
            "bio": forms.Textarea(attrs={"class": "form-control", "placeholder": "Artist Bio"}),
            "email": forms.TextInput(attrs={"class": "form-control", "placeholder": "Booking Email"}),
            "website": forms.TextInput(attrs={"class": "form-control", "placeholder": "Social Link"}),
            "city": forms.TextInput(attrs={"class": "form-control", "placeholder": "City"}),
            "country": forms.TextInput(attrs={"class": "form-control", "placeholder": "Country"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control", "placeholder": "Artist Image"}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super(AddArtistForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(AddArtistForm, self).save(commit=False)
        if self.user:
            instance.manager = self.user
        if commit:
            instance.save()
        return instance


class AddPromoterForm(forms.ModelForm):
    class Meta:
        model = Promoter
        fields = ("name", "city", "email", "website", )
        labels = {
            "name": "",
            "city": "",
            "email": "",
            "website": "",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Name"}),
            "city": forms.TextInput(attrs={"class": "form-control", "placeholder": "City"}),
            "email": forms.TextInput(attrs={"class": "form-control", "placeholder": "Email"}),
            "website": forms.TextInput(attrs={"class": "form-control", "placeholder": "Website"}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super(AddPromoterForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(AddPromoterForm, self).save(commit=False)
        if self.user:
            instance.manager = self.user
        if commit:
            instance.save()
        return instance


class AddVenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ("name", "address", "city", "zip_code", "website", "email", "image", )
        labels = {
            "name": "",
            "address": "",
            "city": "",
            "zip_code": "",
            "website": "",
            "email": "",
            "image": "Venue Image or Logo",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Venue Name"}),
            "address": forms.TextInput(attrs={"class": "form-control", "placeholder": "Address"}),
            "city": forms.TextInput(attrs={"class": "form-control", "placeholder": "City"}),
            "zip_code": forms.TextInput(attrs={"class": "form-control", "placeholder": "Zip Code"}),
            "website": forms.TextInput(attrs={"class": "form-control", "placeholder": "Website"}),
            "email": forms.TextInput(attrs={"class": "form-control", "placeholder": "Email"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control", "placeholder": "Image or Logo"}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super(AddVenueForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(AddVenueForm, self).save(commit=False)
        if self.user:
            instance.manager = self.user
        if commit:
            instance.save()
        return instance


class AddEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = (
            "name",
            "event_date",
            "venue",
            "promoter",
            "artists",
            "event_type",
            "genre",
            "event_flyer",
            "description",
        )
        widgets = {
            "event_date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super(AddEventForm, self).__init__(*args, **kwargs)

        if self.user:
            self.fields['venue'].queryset = Venue.objects.filter(manager=self.user)
            self.fields['promoter'].queryset = Promoter.objects.filter(manager=self.user)
            self.fields['artists'].queryset = Artist.objects.filter(manager=self.user)

    def save(self, commit=True):
        instance = super(AddEventForm, self).save(commit=False)
        if self.user:
            instance.manager = self.user
        if commit:
            instance.save()
        return instance


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("avatar", "fav_genre", "fav_artist", )

        labels = {
            "avatar": "Avatar",
            "fav_genre": "Favorite Music Genre",
            "fav_artist": "Favorite Artist",
        }

        widgets = {
            "avatar": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "fav_genre": forms.Select(attrs={"class": "form-control"}),
            "fav_artist": forms.Select(attrs={"class": "form-control"}),
        }


class DallEImageForm(forms.Form):
    image_prompt = forms.CharField(max_length=1000, widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "A vibrant and captivating image featuring the iconic Taj Mahal..."
        }
    ),
        label=""
    )


class GPTAssistantsApiForm(forms.Form):
    prompt = forms.CharField(
        max_length=850,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "A techno party at the lake..."
            },
        ),
        label="",
        required=True
    )
