from django.urls import path
from . import views

urlpatterns = [
    path('student_courses_list/', views.course_list, name='student_courses_list')
]