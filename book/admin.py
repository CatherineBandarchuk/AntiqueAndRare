from django.contrib import admin

from .models import Book, AgeGroupCategory

admin.site.register(Book)
admin.site.register(AgeGroupCategory)