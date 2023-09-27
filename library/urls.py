from django.urls import path
from . import views

urlpatterns = [
    path('', views.LibraryView.as_view()),
    path('new_author/', views.AuthorView.as_view()),
    path('new_books/', views.NewBook.as_view()),
]
