from django import forms
from . import models


class BlogsForm(forms.Form):
    title = forms.CharField(max_length=100)
    body = forms.CharField(max_length=100)


