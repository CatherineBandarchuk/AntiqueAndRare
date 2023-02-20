from django import forms
from django.forms import ModelForm
from .models import TradeRequest


class CreateRequestForm(ModelForm):
    class Meta:
        model = TradeRequest
        fields = '__all__'