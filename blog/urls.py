from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns =[
	path('news_list/', views.news_list, name='news_list'),
	path('add_news/', views.add_news, name='add_news'),
	path('news/<str:news_slug>/<int:news_pk>/update/', views.news_update, name='news_update'),
	path('news/<str:news_slug>/<int:news_pk>/detail', views.news_detail, name='news_detail'),
	path('news/<str:news_slug>/<int:news_pk>/delete', views.article_delete, name='article_delete')
]
