"""Application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView
from myapp import views
from common.backends import MyRegistrationView
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

# this is my test comment

urlpatterns = [
    path('', views.index, name='home'),
    path('about/',
         TemplateView.as_view(template_name='about.html'),
         name='about'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('register/', TemplateView.as_view(template_name='register.html'),
         name='register'),
    path('posts/create/', views.create_post, name='create_post'),
    path('posts/edit/<int:postid>/', views.edit_post, name='edit_post'),
    path('posts/<int:postid>/', views.post_detail, name='post_detail'),
     path('posts/vote/<int:postid>/', views.vote_post, name='vote_post'),
    # path('accounts/create_post/', views.create_post,
    #      name='create_post'),
    
    path(
        'accounts/password/reset/',
        PasswordResetView.as_view(
            template_name='registration/password_reset_form.html'),
        name="password_reset"),

    path(
        'accounts/password/reset/done/',
        PasswordResetDoneView.as_view(
            template_name='registration/password_reset_done.html'),
        name="password_reset_done"),

    path('accounts/password/reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html'),
        name="password_reset_confirm"),

    path('accounts/password/done/',
        PasswordResetCompleteView.as_view(
            template_name='registration/password_reset_complete.html'),
        name="password_reset_complete"),

    path(
        'accounts/register/', MyRegistrationView.as_view(),
        name='registration_register'),

    path('accounts/create_post/', views.create_post,
        name='registration_create_post'),
        
    path('accounts/', include('registration.backends.simple.urls')),

    path('admin/', admin.site.urls),
]