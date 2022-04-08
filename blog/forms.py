from django import forms
from .models import Comment, Post, Contact


class CommentForm(forms.ModelForm):

    """
    Comment Form
    """

    class Meta:

        """
        Meta Class
        """

        model = Comment
        fields = ('body', )


class PostForm(forms.ModelForm):

    """
    Post Form
    """

    class Meta:

        """
        Meta Class
        """

        model = Post
        fields = (
            'featured_image',
            'title',
            'media_type',
            'genre',
            'name_of_show_or_film',
            'content',
            'status',
            )

