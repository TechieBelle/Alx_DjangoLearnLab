# UPDATE Operation
from bookshelf.models import Book
```python
# Update the title
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()

retrieved_book.title
# Expected Output: 'Nineteen Eighty-Four'