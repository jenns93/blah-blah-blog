from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

MEDIATYPE = ((0, "Film"), (1, "Tv"), (2, "Book"), (3, "other"))

GENRE = (
    (0, "Action"),
    (1, "Adventure"),
    (2, "Sci-fi"),
    (3, "Horror"),
    (4, "Romantic"),
    (5, "Comedy"),
    (6, "Drama"),
    (7, "Thriller"),
    (8, "Rom-com"),
    (9, "Classic"),
    (10, "Historical"),
    (11, "Documentary"),
    (12, "Other"),
)


ISSUE_TYPE = ((0, "Post"), (1, "Comment"), (2, "User"), (3, "Profile"), (4, "Other"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    name_of_show_or_film = models.CharField(max_length=200, unique=True)
    media_type = models.IntegerField(choices=MEDIATYPE, default=0)
    genre = models.IntegerField(choices=GENRE, default=0)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField("image", default="placeholder")
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name="blogpost_like", blank=True)
    dislikes = models.ManyToManyField(User, related_name="blogpost_dislike", blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def number_of_dislikes(self):
        return self.dislikes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class Contact(models.Model):
    name = models.CharField(max_length=200, unique=True)
    username = models.CharField(max_length=200, unique=True)
    related_post = models.CharField(max_length=200, unique=True)
    related_author = models.CharField(max_length=200, unique=True)
    issue_type = models.IntegerField(choices=ISSUE_TYPE, default=0)
    issue_details = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)