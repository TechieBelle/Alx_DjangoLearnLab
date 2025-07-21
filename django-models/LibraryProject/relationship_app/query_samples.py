from relationship_app.models import Author, Book, Library, Librarian

# Sample queries to demonstrate relationships


# query_samples.py
from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"\nBooks by {author.name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with name '{author_name}'")

# 2. List all books in a specific library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"\nBooks in {library.name}:")
        for book in books:
            print(f"- {book.title} (by {book.author.name})")
    except Library.DoesNotExist:
        print(f"No library found with name '{library_name}'")

# 3. Retrieve the librarian for a specific library
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"\nLibrarian for {library.name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with name '{library_name}'")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library.name}")

# Example usage (uncomment when running in a Django environment)
# books_by_author("Chinua Achebe")
# books_in_library("Central Library")
# librarian_for_library("Central Library")
