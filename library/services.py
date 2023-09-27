from . import models
from . import forms

from django.db import connection


def get_all_books() -> models.Book:
    query = models.Book.objects.select_related('author').all()
    return query


def get_all_authors() -> models.Author:
    return models.Author.objects.all()


def create_new_author(form: forms.AuthorForm) -> models.Author:
    author = models.Author(
        first_name=form.cleaned_data['first_name'],
        s_name=form.cleaned_data['s_name'],
        l_name=form.cleaned_data['l_name'],
    )
    author.save()
    return author


def create_new_book(form: forms.BookForm) -> models.Book:
    book = models.Book(
        title=form.cleaned_data['title'],
        isbn=form.cleaned_data['isbn'],
        author=form.cleaned_data['author'],
    )
    return book
