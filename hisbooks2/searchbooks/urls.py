from django.urls import path
from .views import booksearch, do_booksearch, index2, index3

urlpatterns = [
    path('', booksearch, name='searchpage'),
    path('<str:title>', do_booksearch, name='searchpage'),
    path('index3', index3, name='index3'),
]
