from django.shortcuts import render
from django.views.generic.detail import DetailView
from . models import Book, Author, Librarian
from .models import Library


# Create your views here.
def book_list(request):
     book = Book.objects.all()
     context = {
            'books': book
     }
     return render(request, 'relationship_app/list_books.html', context)  


class LibraryView(DetailView):
     model = Library
     template_name = 'relationship_app/library_detail.html'
     context_object_name = 'library'

   