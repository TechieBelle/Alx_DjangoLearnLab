from django.urls import path, include
from .import views
from.views import Index, LoginView, LogoutView, RegisterView, ProfileView


urlpatterns = [
    path('',Index.as_view(), name = 'home'),  
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    
]