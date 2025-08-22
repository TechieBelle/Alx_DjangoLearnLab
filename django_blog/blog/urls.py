from django.urls import path, include
from .import views
from .views import Index, RegisterView, profile_view


urlpatterns = [
     
    path('register/', RegisterView.as_view(), name='register'),
    path("profile/", views.profile_view, name="profile"),
    
]