from django.contrib.auth.models import User
from django.db import models
from django.http import request


class Book(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateTimeField(verbose_name='date-time', auto_now=False)
    authors = models.ManyToManyField(User, related_name='books')
    description = models.TextField(verbose_name='описание', null=True)
    likes = models.PositiveIntegerField(verbose_name="Лайки", default=0)

    def __str__(self):
        return f"{self.title}....... {self.id}"


class Comment(models.Model):
    comment = models.TextField(verbose_name='comment')
    date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_comment')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_comment')
    likes = models.PositiveIntegerField(default=0)


class LikeBookUser(models.Model):
    class Meta:
        unique_together = ("book", "user")

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, **kwargs):
        try:
            super().save(**kwargs)

        except:
            LikeBookUser.objects.get(user=self.user, book=self.book).delete()
            self.book.likes -= 1
        else:
            self.book.likes += 1

        self.book.save()


class LikeCommentUser(models.Model):
    class Meta:
        unique_together = ("comment", "user")

    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, **kwargs):
        try:
            super().save(**kwargs)

        except:
            LikeCommentUser.objects.get(user=self.user, comment_id=self.comment).delete()
            self.comment.likes -= 1
        else:
            self.comment.likes += 1

        self.comment.save()
