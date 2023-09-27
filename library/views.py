from django.shortcuts import render
from django.views import View

from .services import (
    get_all_books,
    get_all_authors,
    create_new_author,
    create_new_book,
)

from . import forms


class LibraryView(View):

    def get(self, request):
        contex = {
            'books': get_all_books()
        }
        return render(request, 'library/books.html', contex)


class AuthorView(View):

    def get(self, request):
        contex = {
            'content': None,
            'form': forms.AuthorForm()
        }

        if request.GET.get('all_authors', False):
            contex['content'] = get_all_authors()

        return render(request, 'library/new_author.html', contex)

    def post(self, request):
        context = {
            'form': forms.AuthorForm()
        }
        if request.POST:
            form = forms.AuthorForm(request.POST)
            if form.is_valid():
                author = create_new_author(form)
                context['content'] = get_all_authors()
        return render(request, 'library/new_author.html', context)


class NewBook(View):

    def get(self, request):
        context = {
            'content': None,
            'form': forms.BookForm()
        }
        return render(request, 'library/new_book.html', context)
    
    
    def post(self, request):
        context = {
            'content': None,
            'form': forms.BookForm()
        }
        if request.POST:
            form = forms.BookForm(request.POST)
            if form.is_valid():
                book = create_new_book(form)
                context['content'] = book
        return render(request, 'library/new_book.html', context)
