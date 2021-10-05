from django.contrib import auth
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from django.contrib.auth import views as auth_views


app_name = 'user_app'
urlpatterns = [
  path('login/', auth_views.LoginView.as_view(template_name='user_app/login.html'), name='login'),
  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
  path('signup/', views.signup, name='signup'), 
  path('user/<int:user_id>/', views.detail, name='detail'), 
  path('user/edit/<int:user_id>/', views.edit, name='edit'),
  path('user/delete/<int:user_id>/', views.delete, name='delete'),
]