from django.contrib import admin
from django.urls import path, include
from students import views
from two_factor.urls import urlpatterns as tf_urls
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    path('', include(tf_urls), name='two_factor'),
    
    path('password_reset/', PasswordResetView.as_view(
        template_name = 'password_reset/reset_password.html'), 
    name='password_reset'),

    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name = 'password_reset/password_reset_done.html'), 
    name='password_reset_done'),
    
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name = 'password_reset/password_reset_confirm.html'), 
    name='password_reset_confirm'),

    path('password_reset/complete/', PasswordResetCompleteView.as_view(
      template_name = 'password_reset/password_reset_complete.html'), 
    name='password_reset_complete'),
]
