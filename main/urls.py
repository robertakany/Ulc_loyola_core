from django.contrib import admin
from django.urls import path
from main import views

urlpatterns=[
path('', views.home, name='home'),
path('cultural_activity/', views.activity, name='activity'),
path('bde/', views.bde, name='bde'),
path('academic_secretariat/', views.academic_secretariat, name='academic_secretariat'),
path('rectorat/', views.rectorat, name='rectorat'),
path('secretariat_administratif/', views.administratif_secretariat ,name='secretariat_administratif'),
path('administractif_du_budget/', views.administratif_du_budget, name='administractif_du_budget'),
path('philosophy_faculty/', views.philosopie, name='philosophy_faculty'),
path('science_and_technology/', views.science_and_technology, name='science_and_technology'),
path('agronomiques_and_veterinaires/',views.agronomiques_et_veterinaires, name='agronomiques_and_veterinaires'),
path('business_administration/',views.business_administration, name='business_administration'),
path('social_sciences_and_management/', views.social_sciences_and_management, name='social_sciences_and_management'),
path('all_courses_list/', views.all_courses_list, name='all_courses_list'),
path('alumnis/', views.alumnis, name='alumnis'),
path('the_registration', views.the_registration, name='the_registration'),
path('contact/', views.contact, name='contact'),
path('about/', views.about, name='about'),



]