from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver

class AgeGroupCategory(models.Model):
    name = models.CharField(max_length=255)

    class Meta: 
        ordering = ('name',)
        verbose_name_plural = 'Age Group Categories'

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255, blank=True, null=True)
    age_group = models.ForeignKey(AgeGroupCategory, related_name='books', on_delete=models.SET_DEFAULT, default='Other') 
    image = models.ImageField(upload_to='book_images', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    owner_user_id = models.ForeignKey('account.CustomUser', related_name='books', on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title