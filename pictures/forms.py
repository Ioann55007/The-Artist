from django import forms
from django.forms import ModelForm
from django.http import request

from .models import Review


class ReviewForm(ModelForm):



    class Meta:
        model = Review
        fields = ('content',)
