from django.urls import path
from . import views
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('', views.list_books, name='list_books'),  # URL for listing books
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_list'),  # URL for listing libraries
    path('login/', views.login_view, name='login'),  # URL for login view
    path('logout/', views.logout_view, name='logout'),  # URL for logout view   
]