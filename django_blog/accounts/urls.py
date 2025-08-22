from django.urls import path

from . import views
from .views import RegisterView, profile_view

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", views.profile_view, name="profile"),
    
]
