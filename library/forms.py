from django import forms
from . import models


class AuthorForm(forms.ModelForm):

    class Meta:
        model = models.Author
        fields = "__all__"


class BookForm(forms.ModelForm):
    isbn = forms.CharField()

    class Meta:
        model = models.Book
        fields = "__all__"
