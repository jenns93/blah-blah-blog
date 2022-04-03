from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm, PostForm


def create_post(request):
    """
    renders create post page
    """
    post_form = PostForm(request.POST or None, request.FILES or None)
    context = {
        'post_form': post_form,
    }

    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form = post_form.save(commit=False)
            post_form.author = request.user
            post_form.save()
            return redirect('home')
    else:
        post_form = PostForm()
    return render(request, "blog_form.html", context)


def edit_post(request, slug):
    """
    renders edit post page
    """
    post = get_object_or_404(Post, slug=slug)
    post_form = PostForm(request.POST or None, instance=post)
    context = {
        'post_form': post_form,
        'post' : post
    }

    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES, instance=post)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('profile')
    else:
        post_form = PostForm(instance=post)
    return render(request, "edit_post_form.html", context)



class PostListProfile(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "profile.html"
    paginate_by = 6


    def userprofile(self, request):
        user = self.request.user
        user_posts = Post.objects.filter(user=self.request.author).order_by('created_on')
        template = 'profile.html'
        return render(request, template, {'user_posts': user_posts, 'user':user})


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
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("created_on")

        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        disliked = False
        if post.dislikes.filter(id=self.request.user.id).exists():
            disliked = True

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
