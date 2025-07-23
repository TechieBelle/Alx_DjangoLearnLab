import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # Query 1: All books by a specific author using filter()
    author_name = "Jane Austen"
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)  # ✅ Required
    print(f"Books by {author.name}: {[book.title for book in books_by_author]}")

    # Query 2: All books in a library using variable
    library_name = "City Library"
    library = Library.objects.get(name=library_name)  # ✅ Required
    books_in_library = library.books.all()
    print(f"Books in {library.name}: {[book.title for book in books_in_library]}")

    # Query 3: Retrieve librarian using reverse OneToOne
    librarian = Librarian.objects.get(library=library)  # ✅ Required
    print(f"Librarian for {library.name}: {librarian.name}")

if __name__ == "__main__":
    run_queries()
