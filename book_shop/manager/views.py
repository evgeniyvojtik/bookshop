from django.shortcuts import render, redirect
from django.views import View

from manager.models import Book, Comment, LikeBookUser, LikeCommentUser


class MyPage(View):

    def get(self, request):
        context = Book.objects.all()
        return render(request, 'index.html', {"context": context})


class AddLike(View):
    def get(self, request, id):
        if request.user.is_authenticated:
            LikeBookUser.objects.create(user=request.user, book_id=id)
        return redirect('the-main-page')


class AddCommentLike(View):
    def get(self, request, id):
        if request.user.is_authenticated:
            LikeCommentUser.objects.create(user=request.user, comment_id=id)
        return redirect('the-main-page')


