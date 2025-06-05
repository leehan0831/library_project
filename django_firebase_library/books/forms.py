# LibraryManagement/forms.py
from django import forms

class BookForm(forms.Form):
    id = forms.IntegerField(label='ID')
    title = forms.CharField(label='Book Title', max_length=100)
    author = forms.CharField(label='Author Name', max_length=100)
    genre = forms.CharField(label='Genre', max_length=50)