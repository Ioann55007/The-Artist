from django import forms
from django.forms import ModelForm
from django.http import request

from .models import Review


class ReviewForm(ModelForm):
    content = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'cols': 80, 'rows': 10}))


    class Meta:
        model = Review
        fields = ('content',)

