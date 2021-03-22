from django import forms
from . import models

class GenreForm(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = ['name','description']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = ['name','description']

class PublisherForm(forms.ModelForm):
    class Meta:
        model = models.Publisher
        fields = ['name','description']

class SeriesForm(forms.ModelForm):
    class Meta:
        model = models.Series
        fields = ['name','description']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ['name','description']

class FormatForm(forms.ModelForm):
    class Meta:
        model = models.Format
        fields = ['name','description']