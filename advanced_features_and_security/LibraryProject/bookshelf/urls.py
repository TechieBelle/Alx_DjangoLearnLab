from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books, LibraryDetailView
from . import views

urlpatterns = [
    path('books/', views.book_list, name='list_books'),  # Function-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Class-based view

    path('login/', LoginView.as_view(template_name='bookshelf/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='bookshelf/logout.html'), name='logout'),
    path('register/', views.register, name='register'),

    #TAsk 3: Role-based views
     path('admin-role/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),

    # Task 4: CRUD operations for Book model
     path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('book_delete/<int:pk>/', views.delete_book, name='delete_book'),

     path('example-search/', views.example_search_view, name='example_search'),
]
