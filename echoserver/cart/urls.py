from django.urls import path
from . import views

urlpatterns = [
    path('add_to_cart/<int:book_id>/', views.add_to_cart_view, name='add_to_cart'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart_view, name='remove_from_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('create_order/', views.create_order_view, name='create_order'),
    path('order_detail/', views.order_detail_view, name='order_detail')
]