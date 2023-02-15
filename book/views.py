from django.shortcuts import render, get_object_or_404
from .models import Book

def detail(request, pk):
    book = get_object_or_404(Book, pk=pk)

    return render(request, 'book/detail.html', {
        'book': book
    })