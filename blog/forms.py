from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "featured_image",
            "title",
            "slug",
            "excerpt",
            "media_type",
            "genre",
            "name_of_show_or_film",
            "content",
            "status",
        )
