from django.urls import path

from manager.views import MyPage, AddCommentLike, AddRate, BookDetail, GenresPage, AddBook, LoginView, logout_user, \
    addcomment, delete_book, main_page_return, UpdateBook

urlpatterns = [
    path('add_comment_like/<int:id>/', AddCommentLike.as_view(), name='comment_like'),
    path('add_comment_like/<int:id>//<str:slug>/', AddCommentLike.as_view(), name='comment_like_location'),
    path('add_rate/<int:rate>/,/<str:slug>/', AddRate.as_view(), name='add_rating'),
    path('add_rate/<int:rate>/,/<str:slug>/,/<int:location>/', AddRate.as_view(), name='add_rating_location'),
    path('book_detail/<str:slug>/', BookDetail.as_view(), name='book-detail-page'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('add_comment/<str:slug>', addcomment, name='add_comment'),
    path('genres_page/<str:genre>/', GenresPage.as_view(), name='genre_page'),
    path('delete_book/<str:slug>/', delete_book, name='delete_book'),
    path('update_book/<str:slug>/', UpdateBook.as_view(), name='update_book'),
    path('add-book/', AddBook.as_view(), name='add_book'),
    path('to_main_page', main_page_return, name='to_main_page'),
    path('', MyPage.as_view(), name='the-main-page'),
]
