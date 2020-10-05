from django.contrib import admin
from django.urls import path,include
from Student import views

urlpatterns = [
    path('', views.studyHome, name = 'teachHome'),
    path('signup', views.handleSignUp, name = 'handleSignUp'),
    path('login', views.loginUser, name = 'login'),
    path('logout', views.logoutUser, name = 'logout'),
    path('dashboard', views.dashboard, name = 'dashboard'),
    path('profile', views.profile, name = 'profile'),
    path('course', views.course, name = 'course'),
    path('enroll', views.enroll, name = 'enroll'),
    path('chat', views.chat, name = 'chat'),
    path('send', views.send, name = 'send'),
]
