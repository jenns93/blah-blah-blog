from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm, PostForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")

        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        disliked = False
        if post.dislikes.filter(id=self.request.user.id).exists():
            disliked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "disliked": disliked,
                "comment_form": CommentForm(),
                "post_form": PostForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-created_on")

        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        disliked = False
        if post.dislikes.filter(id=self.request.user.id).exists():
            disliked = True

        post_form = PostForm(data=request.POST)

        if post_form.is_valid():
            post_form.instance.email = request.user.email
            post_form.instance.name = request.user.username
            post = post_form.save(commit=False)
            post.post = post
            post.save()
        else:
            post_form = PostForm()

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "posted": True,
                "liked": liked,
                "disliked": disliked,
                "comment_form": CommentForm(),
                "post_form": PostForm(),
            },
        )


class Postlike(View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
            post.dislikes.remove(request.user)

        return HttpResponseRedirect(reverse("post_detail", args=[slug]))


class Postdislike(View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.dislikes.filter(id=request.user.id).exists():
            post.dislikes.remove(request.user)
        else:
            post.dislikes.add(request.user)
            post.likes.remove(request.user)

        return HttpResponseRedirect(reverse("post_detail", args=[slug]))

class Add_Blog_Post(SuccessMessageMixin, CreateView):
    """Adds Blog Post"""
    model = Post
    form_class = PostForm
    template_name = 'blog_form.html'
    success_message = 'Blog post successfully added'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

        
