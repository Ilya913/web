from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name_book', 'author_book', 'price_book', 'genre_book', 'publication_year_book','publisher_book']