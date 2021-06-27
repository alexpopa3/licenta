from os import name
from django import template
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


app_name='students'



urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('logout/', views.logoutuser, name = 'logoutuser'),
    path('password/', views.change_password, name='change_password'),
    path('input_reason/', views.input_reason, name='input_reason'),
    path('certificate/', views.certificate, name="certificate"),
    path('question/', views.input_question, name="question"),
    path('all_mine/', views.all_mine, name="all_mine"),
    path('forum/', views.view_questions, name="forum"),
    path('forum/<int:question_id>/', views.detail_question, name='detail_question'),
    path('forum/<int:question_id>/delete', views.delete_question, name = 'delete_question'),
    path('all_mine/<int:question_id>/delete', views.delete_question1, name = 'delete_question1'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)