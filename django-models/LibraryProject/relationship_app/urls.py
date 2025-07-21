from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('', views.book_list, name='book_list'),  # URL for listing books
    path('libraries/<int:pk>/', views.LibraryView.as_view(), name='library_list'),  # URL for listing libraries
]