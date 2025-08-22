from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path,include
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Registration & profile from our app
    path("", include("blog.urls")),   # register, profile
    path('admin/', admin.site.urls),
    # path('', include('blog.urls')),  # Include the blog app's URLs
    
    # Auth views (login/logout) using Django built-ins
    path("login/",  auth_views.LoginView.as_view(template_name="accounts/registration/login.html"), name="login"),
    path(
        "logout/",
        LogoutView.as_view(template_name="accounts/logout.html"),
        name="logout",
    ),

    
]
