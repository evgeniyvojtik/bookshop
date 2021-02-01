from django.urls import path

from manager.views import MyPage, AddCommentLike, AddRate, BookDetail, GenresPage, AddBook, LoginView, logout_user

urlpatterns = [
    path('add_comment_like/<int:id>/', AddCommentLike.as_view(), name='comment_like'),
    path('add_comment_like/<int:id>//<str:slug>/', AddCommentLike.as_view(), name='comment_like_location'),
    path('add_rate/<int:rate>/,/<str:slug>/', AddRate.as_view(), name='add_rating'),
    path('add_rate/<int:rate>/,/<str:slug>/,/<int:location>/', AddRate.as_view(), name='add_rating_location'),
    path('book_detail/<str:slug>/', BookDetail.as_view(), name='book-detail-page'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('genres_page/<str:genre>/', GenresPage.as_view(), name='genre_page'),
    path('add-book/', AddBook.as_view(), name='add_book'),
    path('', MyPage.as_view(), name='the-main-page'),
]
