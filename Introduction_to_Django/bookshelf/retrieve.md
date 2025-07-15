# RETRIEVE Operation
from bookshelf.models import Book
```python
# Retrieve the created book
retrieved_book = Book.objects.get(id=book.id)
retrieved_book.title, retrieved_book.author, retrieved_book.publication_year
# Expected Output: ('1984', 'George Orwell', 1949)