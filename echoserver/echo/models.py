from django.db import models

class Book(models.Model):
    id_book = models.AutoField(primary_key=True)
    name_book = models.CharField(max_length=64, verbose_name="Название книги")
    author_book = models.CharField(max_length=64, verbose_name="Автор книги")
    price_book = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена книги")
    genre_book = models.CharField(max_length=64, verbose_name="Жанр книги")
    publication_year_book = models.IntegerField(verbose_name="Год публикации книги")
    publisher_book = models.CharField(max_length=64, verbose_name="Издательство книги")

    class Meta:
        db_table = 'books'

    def __str__(self):
        return self.name_book
