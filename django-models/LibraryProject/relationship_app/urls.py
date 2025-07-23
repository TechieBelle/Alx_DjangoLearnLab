from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import list_books, LibraryDetailView, RegisterView

urlpatterns = [
    path('', views.list_books, name='list_books'),  # URL for listing books
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_list'),  # URL for listing libraries
    path('login/', LoginView.as_view(template_name = 'relationship_app/login.html'), name='login'),  # URL for login view
    path('logout/', LogoutView.as_view(), name='logout'),  # URL for logout view
    path('register/', RegisterView.as_view(), name='register'),

]
