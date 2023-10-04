from django.urls import path
from . import views

urlpatterns = [
    path('add_course/', views.add_course, name='add_course'),
    path('courses_list/', views.courses_list, name="courses_list"),
    path('<str:teacher_slug>/teacher_admin', views.teacher_admin, name="teacher_admin")
]
