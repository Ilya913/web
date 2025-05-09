from django.db import models
from django.conf import settings
from echo.models import Book

class Cart(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"
        ordering = ['-created_at']

    def __str__(self):
        return f"Корзина пользователя {self.user.username}"

    @property
    def total_price(self):
        return sum(item.total_price for item in self.cartitem_set.all())

class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        verbose_name="Корзина"
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        verbose_name="Книга"
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name="Количество"
    )
    added_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата добавления"
    )

    class Meta:
        verbose_name = "Элемент корзины"
        verbose_name_plural = "Элементы корзины"
        ordering = ['-added_at']

    def __str__(self):
        return f"{self.quantity} x {self.book.name_book}"

    @property
    def total_price(self):
        return self.book.price_book * self.quantity

class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        verbose_name="Пользователь"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="Итоговая сумма заказа"
    )

    def __str__(self):
        return f"Заказ #{self.id} ({self.user.username})"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ['-created_at']

    @property
    def order_number(self):
        return f"ORD-{self.created_at.year}-{self.id}"

class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name="Заказ"
    )
    book_name = models.CharField(
        max_length=64,
        verbose_name="Название книги"
    )
    book_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена книги"
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name="Количество"
    )
    def __str__(self):
        return f"{self.quantity} x {self.book_name}"

    @property
    def structure(self):
        return  f"{self.quantity} x {self.book_name}"

    @property
    def total_price(self):
        return self.book_price * self.quantity

    class Meta:
        verbose_name = "Товар в заказе",
        verbose_name_plural = "Товары в заказе"

