from django.urls import path, include
from .import views
from .views import Index, RegisterView, profile_view
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
     
    path('register/', RegisterView.as_view(), name='register'),
    path("profile/", views.profile_view, name="profile"),
    
        # Auth views (login/logout) using Django built-ins
    path("login/",  auth_views.LoginView.as_view(template_name="accounts/registration/login.html"), name="login"),
    path(
        "logout/",
        LogoutView.as_view(template_name="accounts/logout.html"),
        name="logout",
    ),

]