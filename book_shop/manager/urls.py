from django.urls import path

from manager.views import MyPage, AddLike, AddCommentLike, AddRate

urlpatterns = [
    path('add_like/<int:id>/', AddLike.as_view(), name='add_like'),
    path('add_comment_like/<int:id>/', AddCommentLike.as_view(), name='comment_like'),
    path('add_rate/<int:rate>/,/<int:id>/', AddRate.as_view(), name='add_rating'),
    path('', MyPage.as_view(), name='the-main-page'),


]