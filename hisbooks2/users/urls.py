from django.contrib.auth import login
from django.urls import path, include
from .views import signup, logout_view, login_view

urlpatterns = [
    path('', login_view, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout_view, name='signout')
    # path('login', login, name='login'),
    # path('', include('django.contrib.auth.urls')),
]
