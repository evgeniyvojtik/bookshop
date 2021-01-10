from django.urls import path

from manager.views import MyPage

urlpatterns = [
    path('', MyPage.as_view(), name='the-main-page')
]