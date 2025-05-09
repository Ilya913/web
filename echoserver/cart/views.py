from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem, Order, OrderItem
from echo.models import Book
from django.http import HttpResponseRedirect

@login_required
def add_to_cart_view(request, book_id):
    book = get_object_or_404(Book, id_book = book_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        book=book,
        defaults={'quantity':1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, "Книга добавлена в корзину")
    else:
        messages.success(request,"Книга добавлена в корзину")

    return redirect('echo:home')

@login_required
def remove_from_cart_view(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    book_name = cart_item.book.name_book
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    messages.success(request, f"Книга '{book_name}' удалена из корзины")
    return redirect('cart')

@login_required
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()
    return render(request, 'cart/cart.html', {'cart': cart, 'cart_items': cart_items})

@login_required
def create_order_view(request):
    cart = get_object_or_404(Cart, user=request.user)
    if not cart.cartitem_set.exists():
        messages.error(request, "Для оформления заказа добавьте товары")
        return redirect('cart')

    order = Order.objects.create(
        user = request.user,
        total_price=cart.total_price
    )

    for cart_item in cart.cartitem_set.all():
        OrderItem.objects.create(
            order=order,
            book_name=cart_item.book.name_book,
            book_price=cart_item.book.price_book,
            quantity=cart_item.quantity
        )

    cart.cartitem_set.all().delete()

    return redirect('order_detail')

@login_required
def order_detail_view(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'cart/order.html',{'orders': orders})

