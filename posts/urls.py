from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:post_pk>/', views.detail, name='detail'),
    path('<int:post_pk>/comment', views.comment_create, name='comment_create'),
    path('<int:post_pk>/answer/<str:answer>/', views.answer, name='answer'),
    path('<int:post_pk>/likes/', views.likes, name='likes'),
    path('<int:post_pk>/delete/', views.delete, name='delete'),
    path('<int:post_pk>/update/', views.update, name='update'),
]
