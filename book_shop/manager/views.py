from django.db.models import Count, Prefetch, Avg
from django.shortcuts import render, redirect
from django.views import View

from manager.models import Book, Comment, LikeCommentUser, UsersRating


class MyPage(View):

    def get(self, request):
        context = {}
        comment_query = Comment.objects.annotate(count_like=Count('users_like'))
        comments = Prefetch('comments', comment_query)
        books = Book.objects.prefetch_related("authors", comments)
        context['books'] = books
        context['range'] = range(1, 6)
        return render(request, 'index.html', context)

class AddCommentLike(View):
    def get(self, request, id, slug=None):
        if request.user.is_authenticated:
            LikeCommentUser.objects.create(user=request.user, comment_id=id)
        if slug is None:
            return redirect('the-main-page')
        return redirect('book-detail-page', slug)

class AddRate(View):
    def get(self, request, rate, slug, location=None):
        if request.user.is_authenticated:
            book_id = Book.objects.get(slug=slug).id
            UsersRating.objects.create(user=request.user, book_id=book_id, rate=rate)
        if location is None:
            return redirect('the-main-page')
        return redirect('book-detail-page', slug=slug)


class BookDetail(View):
    def get(self, request, slug):
        context = {}

        comment_query = Comment.objects.annotate(count_like=Count('users_like'))
        comments = Prefetch('comments', comment_query)
        context['book'] = Book.objects.prefetch_related('authors', comments).get(slug=slug)
        context['range'] = range(1, 6)
        return render(request, 'book_detail.html', context)

class GenresPage(View):

    def get(self, request, genre):
        books = Book.objects.filter(genres=genre)
        context = {}
        context['books'] = books.prefetch_related('authors')
        context['range'] = range(1,6)
        return render(request, 'genre_page.html', context)
