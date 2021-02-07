from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.db.models import Count, Prefetch, OuterRef, Exists
from django.shortcuts import render, redirect
from django.views import View
from manager.forms import BookForm, CustomAuthenticationForm, CommentForm
from manager.models import Book, Comment, LikeCommentUser, UsersRating


class MyPage(View):

    def get(self, request):
        context = {}

        books = Book.objects.prefetch_related("authors").order_by("date")
        if request.user.is_authenticated:
            is_owner = Exists(User.objects.filter(books=OuterRef('pk'), id=request.user.id))
            books = books.annotate(is_owner=is_owner)
        context['books'] = books
        context['range'] = range(1, 6)
        context['form'] = BookForm()
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
        context["comment_form"] = CommentForm(data=request.POST)
        return render(request, 'book_detail.html', context)


class GenresPage(View):

    def get(self, request, genre):
        books = Book.objects.filter(genres=genre)
        context = {}
        context['books'] = books.prefetch_related('authors')
        context['range'] = range(1, 6)
        return render(request, 'genre_page.html', context)


class AddBook(View):

    def post(self, request):
        if request.user.is_authenticated:
            bf = BookForm(data=request.POST)
            book = bf.save(commit=True)
            book.authors.add(request.user)
            book.save()
            return redirect('the-main-page')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {'form': CustomAuthenticationForm()})

    def post(self, request):
        user = CustomAuthenticationForm(data=request.POST)
        if user.is_valid():
            login(request, user.get_user())
        return redirect('the-main-page')


def logout_user(request):
    logout(request)
    return redirect('the-main-page')


def addcomment(request, slug):
    form = CommentForm(request.POST)
    if form.is_valid():
        cf = form.save(commit=False)
        cf.author = request.user
        cf.book = Book.objects.get(slug=slug)
        cf.save()
    return redirect('book-detail-page', slug=slug)


def delete_book(request, slug):
    if request.user.is_authenticated:
        book = Book.objects.get(slug=slug)
        if request.user in book.authors.all():
            book.delete()
    return redirect('the-main-page')

class UpdateBook(View):
    def get(self, request, slug):
        if request.user.is_authenticated:
            book = Book.objects.get(slug=slug)
            if request.user in book.authors.all():
                form = BookForm(instance=book)
                return render(request, 'update_book.html', {"form": form, 'slug': book.slug})


    def post(self, request, slug):
        book = Book.objects.get(slug=slug)
        if request.user.is_authenticated:
            bf = BookForm(instance=book, data=request.POST)
            bf.save(commit=True)
        return redirect('the-main-page')

def main_page_return(request):
    return redirect('the-main-page')
