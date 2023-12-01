from django.urls import path
from .views import main_page, main_about, register_view, login_view

urlpatterns = [
    path('', main_page),
    path('about/', main_about, name='about'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
]