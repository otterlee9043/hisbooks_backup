from django.contrib import admin
from django.urls import path
from .views import courseSearch
from searchbooks.views import do_booksearch

urlpatterns = [
    path('', courseSearch, name='courseSearch'),
    path('<str:title>', do_booksearch, name='searchpage'),

]
