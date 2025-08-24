from django.urls import path, include
from .import views
from .views import IndexView, RegisterView, profile_view
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from .views import (PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,)

urlpatterns = [
     
    path('register/', RegisterView.as_view(), name='register'),
    path("profile/", views.profile_view, name="profile"),
    
        # Auth views (login/logout) using Django built-ins
    path("login/",  auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path(
        "logout/",
        LogoutView.as_view(template_name="accounts/logout.html"),
        name="logout",
    ),
    path("", IndexView.as_view(), name="home"),


# List of all posts
    path("posts/", PostListView.as_view(), name="post-list"),

    # Create a new post
    path("post/new/", PostCreateView.as_view(), name="post-create"),

    # Detail view for a single post
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),

    # Edit an existing post
    path("post/<int:pk>/edit/", PostUpdateView.as_view(), name="post-update"),

    # Delete a post
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),

]