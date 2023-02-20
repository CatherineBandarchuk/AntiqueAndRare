from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import TradeRequest
from book.models import Book


@login_required
def trade(request, pk):
    requested_book = get_object_or_404(Book, pk=pk)
    return render(request, 'trades/option.html', { 'book': requested_book })


@login_required
def select_book(request, pk):
    requested_book = get_object_or_404(Book, pk=pk)