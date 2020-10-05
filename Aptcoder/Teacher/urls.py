from django.contrib import admin
from django.urls import path,include
from Teacher import views

urlpatterns = [
    path('', views.teachHome, name = 'teachHome'),
    path('signup', views.handleSignUp, name = 'handleSignUp'),
    path('login', views.loginUser, name = 'login'),
    path('logout', views.logoutUser, name = 'logout'),
    path('dashboard', views.dashboard, name = 'dashboard'),
    path('profile', views.profile, name = 'profile'),
    path('chat', views.chat, name = 'chat'),
    path('send', views.send, name = 'send'),
]
