from django.urls import path
from . import views

urlpatterns = [
    path('add_course/', views.add_course, name='add_course'),
    path('courses_list/', views.courses_list, name="courses_list"),
    path('course/<int:course_pk>/', views.course_update, name="course_update"),
    path('<str:teacher_slug>/teacher_admin', views.teacher_admin, name="teacher_admin"),
    path('user_profile/', views.edit_user_profile, name='user_profile_edit_teacher_admin')
    
]
