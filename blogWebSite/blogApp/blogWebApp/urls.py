from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blogWebApp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home),
    path('home/', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('topics/', views.blog_category, name='blog-category'),
    path('profile/', views.user_profile, name='user-profile'),
    path('create/', views.create_blog, name='create_blog'),
    path('submit/', views.submit_blog, name='submit_blog'),  # Add name parameter
    path('edit/<int:blog_id>/', views.edit_blog, name='edit_blog'),
    path('update/<int:blog_id>/', views.update_blog, name='update_blog'),
    path('delete/<int:blog_id>/', views.delete_blog, name='delete_blog'),
    path('contact/', views.contact, name='user-contact'),
    path('register/', views.register, name='user-register'),
    path('login/', views.user_login, name='user-login'),
    path('passwordreset/', views.reset_password, name='reset-password'),
    path('logout/', views.user_logout, name='user-logout'),
    path('sendmail/', views.send_user_email, name='send_user_email'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

