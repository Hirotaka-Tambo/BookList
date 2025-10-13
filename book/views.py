from django.shortcuts import render
from django.views.generic import ListView
from .models import Book

class LiseBoolView(ListView):
    template_name = 'book/book_list.html'
    model = Book