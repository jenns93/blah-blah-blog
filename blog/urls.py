from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('blog_form/', views.Add_Blog_Post.as_view(), name='blog_form'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', views.Postlike.as_view(), name='post_like'),
    path('dislike/<slug:slug>/', views.Postdislike.as_view(), name='post_dislike'),
    
]