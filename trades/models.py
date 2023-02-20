from django.db import models

# Create your models here.
# from account.models import CustomUser
from book.models import Book


class TradeRequest(models.Model):
    requested_book = models.ForeignKey(Book, related_name = 'requested_book', on_delete=models.DO_NOTHING)
    offering_book = models.ForeignKey(Book, related_name = 'offering_book', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    closed_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=200, default='pending') # pending or traded or closed
