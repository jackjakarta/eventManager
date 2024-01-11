from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from .models import Promoter, Venue, Event, Profile

AuthUser = get_user_model()


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="",
                             widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Email Address"}))
    first_name = forms.CharField(label="",
                                 max_length=120,
                                 widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "First Name"}))
    last_name = forms.CharField(label="",
                                max_length=120,
                                widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Last Name"}))

    class Meta:
        model = AuthUser
        fields = ("first_name", "last_name", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["placeholder"] = "Password"
        self.fields["password1"].label = ""
        self.fields[
            "password1"].help_text = ('<ul class="form-text text-muted small"><li>Your password can\'t be too similar '
                                      'to your other personal information.</li><li>Your password must contain at least '
                                      '8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>'
                                      'Your password can\'t be entirely numeric.</li></ul>')

        self.fields["password2"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm Password"
        self.fields["password2"].label = ""
        self.fields[
            "password2"].help_text = ('<span class="form-text text-muted"><small>Enter the same password as before, '
                                      'for verification.</small></span>')


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


# class AddEventForm(forms.ModelForm):
#     class Meta:
#         model = Event
#         fields = ("name", "event_date", "venue", "promoter", "event_flyer", "description", )
#
#     def __init__(self, *args, **kwargs):
#         self.user = kwargs.pop("user", None)
#         super(AddEventForm, self).__init__(*args, **kwargs)
#
#         if self.user:
#             # Filter venue choices to only those managed by the user
#             self.fields['venue'].queryset = Venue.objects.filter(manager=self.user)
#             # Filter promoter choices to only those managed by the user
#             self.fields['promoter'].queryset = Promoter.objects.filter(manager=self.user)
#
#     def save(self, commit=True):
#         instance = super(AddEventForm, self).save(commit=False)
#         if self.user:
#             instance.manager = self.user
#         if commit:
#             instance.save()
#         return instance


class AddEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ("name", "event_date", "venue", "promoter", "event_flyer", "description", )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super(AddEventForm, self).__init__(*args, **kwargs)

        if self.user:
            self.fields['venue'].queryset = Venue.objects.filter(manager=self.user)
            self.fields['promoter'].queryset = Promoter.objects.filter(manager=self.user)

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
        fields = ("avatar", )

        labels = {
            "avatar": "Avatar",
        }

        widgets = {
            "avatar": forms.ClearableFileInput(attrs={"class": "form-control"})
        }


class DallEImageForm(forms.Form):
    image_prompt = forms.CharField(max_length=1000, widget=forms.TextInput(
        attrs={'placeholder': 'Describe your image...'}),
        label="Image description:"
    )
