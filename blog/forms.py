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


class ContactForm(forms.ModelForm):

    """
    Contact Form
    """

    model = Contact
    fields = (
        'name',
        'username',
        'related_post',
        'related_author',
        'issue_type',
        'issue_details',
        'created_on',
        )
