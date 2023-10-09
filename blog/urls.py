from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns =[
	path('news_list/', views.news_list, name='news_list'),
	path('add_news/', views.add_news, name='add_news'),
	path('news/<str:news_slug>/<int:news_id>/update/', views.news_update, name='news_update'),
	path('news/<str:news_slug>/<int:news_id>/detail', views.news_content, name='news_content'),
	path('news/<str:news_slug>/<int:news_id>/delete', views.article_delete, name='article_delete'),
    path('news/<int:news_id>/add_comment/',views.add_comment, name='add_comment'),
    path('news/<int:news_id>/toggle_like/',
         views.toggle_like, name='toggle_like'),
]
