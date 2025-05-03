from django.urls import path
from . import views

app_name = 'echo'

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_book, name='add_book'),
    path('edit/<int:id_book>/', views.edit_book, name='edit_book'),
    path('delete/<int:id_book>/', views.delete_book, name='delete_book'),
]