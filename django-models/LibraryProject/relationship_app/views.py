from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views.generic.detail import DetailView
from . models import Book, Author, Librarian
from .models import Library


# Create your views here.
def list_books(request):
     book = Book.objects.all()
     context = {
            'books': book
     }
     return render(request, 'relationship_app/list_books.html', context)  


class LibraryDetailView(DetailView):
     model = Library
     template_name = 'relationship_app/library_detail.html'
     context_object_name = 'library'

  
class RegisterView(FormView):
    template_name = 'relationship_app/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')  # change 'home' as appropriate

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)