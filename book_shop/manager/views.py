from django.shortcuts import render
from django.views import View

from manager.models import Book, Comment


class MyPage(View):

    def get(self, request):
        context = Book.objects.all()
        return render(request, 'index.html', {"context": context})

