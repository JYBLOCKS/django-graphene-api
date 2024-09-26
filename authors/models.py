from django.db import models

from books.models import Books

# Create your models here.


class Authors(models.Model):
    name = models.TextField(max_length=100)
    last_name = models.TextField(max_length=150)
    age = models.IntegerField()
    books = models.ManyToManyField(Books)

    def __str__(self) -> str:
        return super().__str__()
