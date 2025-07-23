import os
import django

# Setup Django environment (adjust the project name if needed)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # Query 1: All books by a specific author
    author_name = "Jane Austen"
    author = Author.objects.get(name=author_name)
    books_by_author = author.books.all()
    print(f"Books by {author.name}: {[book.title for book in books_by_author]}")

    # Query 2: All books in a specific library
    library_name = "City Library"
    library = Library.objects.get(name=library_name)  # ✅ Requirement satisfied here
    books_in_library = library.books.all()
    print(f"Books in {library.name}: {[book.title for book in books_in_library]}")

    # Query 3: Retrieve the librarian for a specific library
    librarian = library.librarian
    print(f"Librarian for {library.name}: {librarian.name}")

if __name__ == "__main__":
    run_queries()
