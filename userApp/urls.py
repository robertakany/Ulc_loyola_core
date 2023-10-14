from django.urls import path
from main import views
from django.contrib import admin
from django.urls import path
#from user import views,api_views
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.contrib.auth import views as auth_views
from userApp import views

urlpatterns = [
	path('signup/', views.signup, name='register'),
	path('login/', views.connect, name='login'),
    path('logout', views.disconnect, name='logout'),
	path('<str:user_slug>/update_password/', views.password, name='password'),
	path('upload_profile_photo/', views.upload_profile_photo, name='upload-profile'),
	path('<str:user_slug>/disconnect/', views.deconnexion, name='logout'),
	path('user_profile/', views.edit_user_profile, name='user_profile_edit'),

	path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
	path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]