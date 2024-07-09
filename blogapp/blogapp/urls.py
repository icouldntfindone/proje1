"""blogapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from blog import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from blog.views import CustomLoginView, ResetPasswordView, ChangePasswordView

from blog.forms import LoginForm
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from blog.views import profile,RegisterView # type: ignore
from django.contrib.auth import views as auth_views
from blog.views import CustomLoginView, ResetPasswordView, ChangePasswordView

from blog.forms import LoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),  # register view için URL tanımlanması
    path('main/', views.main, name='main'), 
    path('main2/', views.main2, name='main2'), 
    path('main3/', views.main3, name='main3'),   
    path('blog/', views.create_blog, name='create_blog'),
    path('details/', views.details, name='details'),
    path('forum_list', views.forum_list, name='forum_list'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/', profile, name='profile'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('send_message/', views.send_message, name='send_message'),
    path('inbox/', views.inbox, name='inbox'),
    path('user_messages/<str:username>/', views.user_messages, name='user_messages'),
    path('iletişim/', views.iletişim, name='iletişim'),
    path('complaint_form/', views.complaint_form, name='complaint_form'),
    path('jobs/', views.job_list, name='job_list'),
    path('create/', views.create_job, name='create_job'), 
    path('user_messages/<str:username>/', views.user_messages, name='user_messages'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='blog/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='blog/password_reset_complete.html'),
         name='password_reset_complete'),

    path('password-change/', ChangePasswordView.as_view(), name='password_change'),

    re_path(r'^oauth/', include('social_django.urls', namespace='social')),
    path('blogdet/<str:pk>/',views.blogdet,name='blogdetails'),

   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)