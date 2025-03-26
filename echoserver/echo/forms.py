from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name_book', 'author_book', 'price_book', 'genre_book', 'publication_year_book','publisher_book']
        labels = {
            'name_book': 'Название книги',
            'author_book': 'Автор книги',
            'price_book': 'Цена книги',
            'genre_book': 'Жанр книги',
            'publication_year_book': 'Год публикации книги',
            'publisher_book': 'Издательство книги',
        }