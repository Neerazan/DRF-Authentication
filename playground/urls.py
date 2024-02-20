from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view()),
    path('login/', views.UserLoginView.as_view()),
    path('hello/', views.say_hello)
]