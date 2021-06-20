from django.urls import path
from .views import PostUpload, do_usedbooksearch, upload, complain, create_comment
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', PostUpload.as_view(), name='index4'),
    path('<str:book_title>', do_usedbooksearch, name='search'),
    path('upload/', upload, name='upload'),
    path('complain/', complain, name='complain'),
    # path('upload_post/', upload_post, name='upload_post'),
    # path('create_comment/', CommentUpload.as_view(), name='create_comment'),
    path('<str:book_title>/create_comment/', create_comment, name='create_comment'),
    # path('submit_post/', PostUpload.as_view(), name='submit_post'),
]