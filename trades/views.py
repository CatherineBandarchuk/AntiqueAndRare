from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from .models import TradeRequest
from book.models import Book
from django.urls import reverse_lazy


class BookListView(generic.ListView, LoginRequiredMixin):
    model = Book
    success_url = reverse_lazy("main:index")
    context_object_name = 'book_list'
    template_name = 'trades/option.html'
    paginate_by = 3

    def get_queryset(self):
        return Book.objects.filter(available=True, owner_user_id=self.request.user)

    def post(self, request, pk):
        requested_book = get_object_or_404(Book, pk=pk)
        offering_book = get_object_or_404(Book, pk=request.POST['mybook'])
        checked = request.POST.getlist('allowchoose')
        option = True if checked else False
        TradeRequest.objects.create(
            requested_book=requested_book,
            offering_book=offering_book,
            option=option
        )
        offering_book.available = False
        offering_book.save()
        return redirect('main:index')


class RequestsListView(generic.ListView, LoginRequiredMixin):
    model = TradeRequest
    context_object_name = 'request_list'
    template_name = 'trades/requests.html'
    paginate_by = 5

    def get_queryset(self):
        return TradeRequest.objects.filter(Q(offering_book__owner_user_id=self.request.user) | Q(requested_book__owner_user_id=self.request.user))

    def post(self, request, pk):
        if request.POST.get('decline'):
            #offering_book = get_object_or_404(Book, pk=request.POST)
            #offering_book.available = True
            #offering_book.save()
            return render(request, 'trades/options.html', {})
        else:
            return render(request, 'trades/requests.html', {})


class OtherBookListView(generic.ListView, LoginRequiredMixin):
    model = Book
    success_url = reverse_lazy("main:index")
    context_object_name = 'other_book_list'
    template_name = 'trades/otheroption.html'
    paginate_by = 3

    def get_queryset(self):
        return Book.objects.filter(available=True, owner_user_id=self.request.user)