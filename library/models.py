from django.db import models


class Author(models.Model):
    first_name = models.CharField(
        max_length=100
    )
    s_name = models.CharField(
        max_length=100
    )
    l_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.s_name} {self.l_name}'


class Book(models.Model):
    title = models.CharField(
        max_length=250
    )
    isbn = models.TextField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.title
