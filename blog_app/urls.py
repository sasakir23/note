from django.urls import path
from . import views


app_name = 'blog_app'

urlpatterns = [
   path('', views.index, name='index'),
   path('detail/<int:post_id>/', views.detail, name='detail'),
   path('add/', views.add, name='add'),
   path('edit/<int:post_id>/', views.edit, name='edit'),
   path('delete/<int:post_id>/', views.delete, name='delete'), 
]