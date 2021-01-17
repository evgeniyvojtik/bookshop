from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateTimeField(verbose_name='date-time', auto_now=False)
    authors = models.ManyToManyField(User, related_name='books')
    description = models.TextField(verbose_name='описание', null=True)
    likes = models.PositiveIntegerField(default=0)
    users_like = models.ManyToManyField(User, through='manager.LikeBookUser', related_name='liked_books')
    genres = models.CharField(max_length=50, verbose_name='жанр', null=True)
    rate = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    users_counted_stars = models.PositiveIntegerField(default=0, verbose_name='counted_stars')
    count_users = models.PositiveIntegerField(default=0, verbose_name='counted_users')

    def __str__(self):
        return f"{self.title}....... {self.id}"


class Comment(models.Model):
    comment = models.TextField(verbose_name='comment')
    date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_comment')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    users_like = models.ManyToManyField(
        User,
        through='manager.LikeCommentUser',
        related_name='liked_comment'
    )


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

    # def save(self, **kwargs):
    #     try:
    #         super().save(**kwargs)
    #
    #     except:
    #         LikeBookUser.objects.get(user=self.user, book=self.book).delete()


class LikeCommentUser(models.Model):
    class Meta:
        unique_together = ("comment", "user")

    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='liked_user_table')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_comment_table')

    def save(self, **kwargs):
        try:
            super().save(**kwargs)

        except:
            LikeCommentUser.objects.get(user=self.user, comment_id=self.comment).delete()


class UsersRating(models.Model):
    class Meta:
        unique_together = ('book', 'user')

    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='users_rate')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='book_rate')
    rate = models.PositiveIntegerField(verbose_name='rating')
    def save(self, **kwargs):
        try:
            super().save(**kwargs)
        except:
            ur = UsersRating.objects.get(book=self.book, user=self.user)
            self.book.users_counted_stars -= ur.rate
            ur.rate = self.rate
            ur.save()

        else:
            self.book.count_users += 1
        self.book.users_counted_stars += self.rate
        self.book.rate = self.book.users_counted_stars / self.book.count_users
        self.book.save()




