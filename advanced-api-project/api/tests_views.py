from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book, Author

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        # Create Authors
        self.author1 = Author.objects.create(name="Author One")
        self.author2 = Author.objects.create(name="Author Two")

        # Create Books
        self.book1 = Book.objects.create(
            title="A Tale of Two Cities",
            author=self.author1,
            publication_year=1859
        )
        self.book2 = Book.objects.create(
            title="Great Expectations",
            author=self.author2,
            publication_year=1861
        )
        self.book3 = Book.objects.create(
            title="Another Story",
            author=self.author1,
            publication_year=2000
        )

    def test_create_book(self):
        url = reverse('book-list')
        data = {
            "title": "New Book",
            "author": self.author1.id,
            "publication_year": 2021
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)

    def test_filter_books_by_author(self):
        url = reverse('book-list')
        response = self.client.get(url, {'author': self.author1.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # book1 & book3

    def test_filter_books_by_publication_year(self):
        url = reverse('book-list')
        response = self.client.get(url, {'publication_year': 1861})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # book2

    def test_search_books_by_title(self):
        url = reverse('book-list')
        response = self.client.get(url, {'search': 'Expectations'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Great Expectations")

    def test_search_books_by_author_name(self):
        url = reverse('book-list')
        response = self.client.get(url, {'search': 'Author One'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # book1 & book3

    def test_order_books_by_title(self):
        url = reverse('book-list')
        response = self.client.get(url, {'ordering': 'title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [book['title'] for book in response.data]
        self.assertEqual(titles, sorted(titles))

    def test_order_books_by_publication_year_desc(self):
        url = reverse('book-list')
        response = self.client.get(url, {'ordering': '-publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years, reverse=True))
