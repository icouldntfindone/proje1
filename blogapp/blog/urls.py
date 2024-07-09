
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from .views import profile,RegisterView
from django.contrib.auth import views as auth_views
from blog.views import CustomLoginView, ResetPasswordView, ChangePasswordView
from .views import search_books
from blog.forms import LoginForm



urlpatterns = [
    path('', views.main, name='anasayfa'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', views.user_login, name='login'),
    path('main3/', views.main3, name='main3'),
    path('main2/', views.main2, name='main2'),
    path('blog/', views.create_blog, name='create_blog'),
    path('details/', views.details, name='details'),
    path('forum_list/', views.forum_list, name='forum_list'),
    path('forum_detail/', views.forum_detail, name='forum_detail'),
    path('profile/', profile, name='profile'),
    path('password_reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('send_message/', views.send_message, name='send_message'),
    path('inbox/', views.inbox, name='inbox'),
    path('iletişim/', views.iletişim, name='iletişim'),
    path('complaint_form/', views.complaint_form, name='complaint_form'),
    path('jobs/', views.job_list, name='job_list'),
    path('create/', views.create_job, name='create_job'),    
    path('sector/', views.job_sector, name='job_sector'),  
    path('odtu/', views.odtu, name='odtu'),
    path('itü/', views.itü, name='itü'),
    path('odtu_hakkında/', views.odtu_hakkında, name='odtu_hakkında'),
    path('gsü/', views.gsü, name='gsü'),
    path('search/', search_books, name='search_books'),
    path('add_book/', views.add_book, name='add_book'),
    path('forum_home', views.forum_home, name='forum_home'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('new_post/', views.new_post, name='new_post'),
    path('post/<int:post_id>/add_comment/', views.add_comment, name='add_comment'),
    path('user_messages/<str:username>/', views.user_messages, name='user_messages'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='blog/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset-complete/<uidb64>/<token>/',
         auth_views.PasswordResetCompleteView.as_view(template_name='blog/password_reset_complete.html'),
         name='password_reset_complete'),

    path('password-change/', ChangePasswordView.as_view(), name='password_change'),

    re_path(r'^oauth/', include('social_django.urls', namespace='social')),
    path('blogdet/<str:pk>/',views.blogdet,name='blogdetails')
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)