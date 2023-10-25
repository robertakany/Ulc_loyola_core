from django.urls import path
from . import views

urlpatterns = [
    path('souscription/', views.souscription, name='student_souscription'),
    path('student_courses_list/', views.course_list, name='student_courses_list'),
    path('student_admin/', views.student_admin, name='student_admin'),
    path('student_profile/',views.edite_student_profile, name='student_profile_edit')
]