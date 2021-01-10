from django.contrib.auth.models import User
from django.db import models



class Book(models.Model):

    title = models.CharField(max_length=250)
    date = models.DateTimeField(verbose_name='date-time', auto_now=False)
    authors = models.ManyToManyField(User, related_name='books')
    description = models.TextField(verbose_name='описание', null=True)

    def __str__(self):
        return f"{self.title}....... {self.id}"


class Comment(models.Model):
    comment = models.TextField(verbose_name='comment')
    date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_comment')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_comment')

