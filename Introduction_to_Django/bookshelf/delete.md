# DELETE Operation

```python
# Delete the book
retrieved_book.delete()
# Expected Output: (1, {'your_app_name.Book': 1})

# Confirm deletion
Book.objects.all()
# Expected Output: <QuerySet []>