from django.urls import path
from .views import PostUpload, do_usedbooksearch, upload, complain, book_sold, popup_booksearch, Insert_bookinfo
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', PostUpload.as_view(), name='index4'),
    path('<str:book_title>', do_usedbooksearch, name='search'),
    path('upload/', upload, name='upload'),
    path('complain/', complain, name='complain'),
    path('complain/<str:complaintee>/<str:complainer>', complain, name='complain'),
    path('book_sold/<str:post_id>', book_sold, name='book_sold'),
    # path('upload_post/', upload_post, name='upload_post'),
    # path('create_comment/', CommentUpload.as_view(), name='create_comment'),
    # path('<str:book_title>/create_comment/', create_comment, name='create_comment'),
    # path('submit_post/', PostUpload.as_view(), name='submit_post'),
    path('popup/<str:course_info>/<str:title>', popup_booksearch, name='popup_booksearch'),
    path('addbook/<str:course_info>/', Insert_bookinfo.as_view(), name='do_popup_booksearch'),
    path('addbook/<str:course_info>/<str:title>/', Insert_bookinfo.as_view(), name='do_popup_booksearch'),
]