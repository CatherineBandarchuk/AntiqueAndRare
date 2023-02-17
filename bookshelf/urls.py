from django.urls import path

from . import views

app_name = 'bookshelf'

urlpatterns = [
    path('', views.index, name='index'),
]