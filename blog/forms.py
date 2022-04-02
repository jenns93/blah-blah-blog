from .models import Comment, Post, Contact
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


class ContactForm(forms.ModelForm):
    model = Contact
    fields = (
        "name",
        "username",
        "related_post",
        "related_author",
        "issue_type",
        "issue_details",
        "created_on",
    )