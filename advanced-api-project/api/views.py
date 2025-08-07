from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated 
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
#A ListView for retrieving all books.
class BookListView(generics.ListAPIView):
   permission_classes = [IsAuthenticatedOrReadOnly]
   queryset = Book.objects.all()
   serializer_class = BookSerializer
   filter_backends = [filters.SearchFilter]  # Can also combine with filtering
   search_fields = ['author', 'publication_year'] # Fields to search in
 
# A DetailView for retrieving a single book by ID.
class BookDetailView(generics.RetrieveAPIView):
   permission_classes = [IsAuthenticatedOrReadOnly]
   queryset = Book.objects.all()
   serializer_class = BookSerializer   

#A CreateView for adding a new book.
class BookCreateView(generics.CreateAPIView):
   #Add permission for aunthentiacted users only
    permission_classes = [IsAuthenticated] #only logged-in users can create books
    queryset = Book.objects.all()
    serializer_class = BookSerializer

   # Add validation rules

# An UpdateView for modifying an existing book.
class BookUpdateView(generics.UpdateAPIView):
    # Add permission for authenticated users only
    permission_classes = [IsAuthenticated]
    srializer_class = BookSerializer
    queryset = Book.objects.all()

   # Add validation rules

# A DeleteView for removing a book.
class BookDeleteView(generics.DestroyAPIView):
    # Add permission for authenticated users only
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer
    queryset = Book.objects.all()