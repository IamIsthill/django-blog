from django.contrib import admin
from django.urls import path, include
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
urlpatterns = [
  # path("", views.home_view, name="blog-home"),
  path("", PostListView.as_view(), name="blog-home"),
  path("user/<str:username>", UserPostListView.as_view(), name="user-posts"),
  path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
  path("post/update/<int:pk>/", PostUpdateView.as_view(), name="post-update"),
  path("post/delete/<int:pk>/", PostDeleteView.as_view(), name="post-delete"),
  path("post/new/", PostCreateView.as_view(), name="post-create"),
  path("about/", views.about_view, name="blog-about"),
]