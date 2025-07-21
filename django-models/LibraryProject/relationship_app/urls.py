from django.urls import path
from . import views
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('', views.list_books, name='list_books'),  # URL for listing books
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_list'),  # URL for listing libraries
]