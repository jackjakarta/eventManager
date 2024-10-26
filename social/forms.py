from django import forms
from .models import Post, PostComment
from website.utils.moderation import check_moderate


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "image",
            "event",
            "description",
        )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super(PostForm, self).__init__(*args, **kwargs)

    def check_for_moderation(self):
        if not check_moderate(self.cleaned_data.get("description")):
            return True
        return False

    def save(self, commit=True):
        instance = super(PostForm, self).save(commit=False)
        if self.user:
            instance.user = self.user
        if commit:
            instance.save()
        return instance


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ("text",)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        self.post = kwargs.pop("post", None)
        super(PostCommentForm, self).__init__(*args, **kwargs)

    def check_for_moderation(self):
        if not check_moderate(self.cleaned_data.get("text")):
            return True
        return False

    def save(self, commit=True):
        instance = super(PostCommentForm, self).save(commit=False)

        if self.user:
            instance.user = self.user
            instance.post = self.post
        if commit:
            instance.save()

        return instance
