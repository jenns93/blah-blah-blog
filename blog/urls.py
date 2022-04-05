from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("profile/", views.PostListProfile.as_view(), name="profile"),
    path("blog_form/", views.create_post, name="blog_form"),
    path("edit_post_form/<slug:slug>/", views.edit_post, name="edit_post_form"),
    path("delete_post/<slug:slug>/", views.delete_post, name="delete_post"),
    path("category/<slug:genre>/", views.post_category, name="category"),
    path("<slug:slug>/", views.PostDetail.as_view(), name="post_detail"),
    path("like/<slug:slug>/", views.Postlike.as_view(), name="post_like"),
    path("dislike/<slug:slug>/", views.Postdislike.as_view(), name="post_dislike"),
]


handler404 = "blog.views.page_not_found_view"
