from django.urls import path
from . import views

urlpatterns = [
    path('student_courses_list/', views.course_list, name='student_courses_list'),
    path('<str:student_slug>/student_admin/', views.student_admin, name='student_admin'),
    path('user_profile/', views.edit_profile, name='user_profile_edit'),
    path('<str:student_slug>/student_profile/',views.edite_student_profile, name='student_profile_edit')
]