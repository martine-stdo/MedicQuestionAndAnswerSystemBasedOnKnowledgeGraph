# users/urls.py
from django.urls import path
from .views import register_user, login_user, chat_view
urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('chat/', chat_view, name='chat'),
]
