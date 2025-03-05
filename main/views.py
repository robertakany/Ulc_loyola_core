from django.shortcuts import render

from students_admin.models import Student
from teachers_admin.models import Teacher
from userApp import User
from university_admin.models import Course,Alumni
from blog.models import New


""" def home(request):
    user = request.user
    teachers = None
    students = None

    if user.is_authenticated:
        print(user.username)
        teachers = Teacher.objects.filter(user=user)
        students = Student.objects.filter(user=user)

    return render(request, 'main/home.html', locals())
 """

def home(request):

    news = New.objects.all().order_by('-created_at')[:3]
    user = request.user
    
    teachers = None
    students = None

    if user.is_authenticated:
        print(user.role)
        print(user.username)
        # Recherchez l'utilisateur actuellement connecté en utilisant son ID
        
        teachers = Teacher.objects.filter(user=user)
        students = Student.objects.filter(user=user)

    return render(request, 'main/home.html', locals())


def contact(request):
    news = New.objects.all().order_by('-created_at')[:3]
    user = request.user
    
    teachers = None
    students = None

    if user.is_authenticated:
        print(user.role)
        print(user.username)
        # Recherchez l'utilisateur actuellement connecté en utilisant son ID
        
        teachers = Teacher.objects.filter(user=user)
        students = Student.objects.filter(user=user)

    return render(request, 'main/contact.html' , locals())

def rectorat(request):
    news = New.objects.all().order_by('-created_at')[:3]
    user = request.user
    
    teachers = None
    students = None

    if user.is_authenticated:
        print(user.role)
        print(user.username)
        # Recherchez l'utilisateur actuellement connecté en utilisant son ID
        
        teachers = Teacher.objects.filter(user=user)
        students = Student.objects.filter(user=user)
    return render(request, 'main/rectorat.html', locals())

def activity(request):
    news = New.objects.all().order_by('-created_at')[:3]
    user = request.user
    
    teachers = None
    students = None

    if user.is_authenticated:
        print(user.role)
        print(user.username)
        # Recherchez l'utilisateur actuellement connecté en utilisant son ID
        
        teachers = Teacher.objects.filter(user=user)
        students = Student.objects.filter(user=user)
    return render(request, 'main/activity.html', locals())

def bde(request):
    news = New.objects.all().order_by('-created_at')[:3]
    user = request.user
    
    teachers = None
    students = None

    if user.is_authenticated:
        print(user.role)
        print(user.username)
        # Recherchez l'utilisateur actuellement connecté en utilisant son ID
        
        teachers = Teacher.objects.filter(user=user)
        students = Student.objects.filter(user=user)
    return render(request, 'main/bde.html', locals())

def academic_secretariat(request):
    news = New.objects.all().order_by('-created_at')[:3]
    user = request.user
    
    teachers = None
    students = None

    if user.is_authenticated:
        print(user.role)
        print(user.username)
        # Recherchez l'utilisateur actuellement connecté en utilisant son ID
        
        teachers = Teacher.objects.filter(user=user)
        students = Student.objects.filter(user=user)
    return render(request, 'main/academic_secretariat.html', locals())

def administratif_secretariat(request):
    news = New.objects.all().order_by('-created_at')[:3]
    user = request.user
    
    teachers = None
    students = None

    if user.is_authenticated:
        print(user.role)
        print(user.username)
        # Recherchez l'utilisateur actuellement connecté en utilisant son ID
        
        teachers = Teacher.objects.filter(user=user)
        students = Student.objects.filter(user=user)
    return render(request, 'main/administratif_secret.html', locals())

def administratif_du_budget(request):
    news = New.objects.all().order_by('-created_at')[:3]
    user = request.user
    
    teachers = None
    students = None

    if user.is_authenticated:
        print(user.role)
        print(user.username)
        # Recherchez l'utilisateur actuellement connecté en utilisant son ID
        
        teachers = Teacher.objects.filter(user=user)
        students = Student.objects.filter(user=user)
    return render(request, 'main/administratif_du_budget.html', locals())

def agronomiques_et_veterinaires(request):
    news = New.objects.all().order_by('-created_at')[:3]
    user = request.user
    
    teachers = None
    students = None

    if user.is_authenticated:
        print(user.role)
        print(user.username)
        # Recherchez l'utilisateur actuellement connecté en utilisant son ID
        
        teachers = Teacher.objects.filter(user=user)
        students = Student.objects.filter(user=user)
    return render(request, 'main/agronomiques_et_veterinaires.html', locals())

def philosopie(request):
    news = New.objects.all().order_by('-created_at')[:3]
    user = request.user
    
    teachers = None
    students = None

    if user.is_authenticated:
        print(user.role)
        print(user.username)
        # Recherchez l'utilisateur actuellement connecté en utilisant son ID
        
        teachers = Teacher.objects.filter(user=user)
        students = Student.objects.filter(user=user)
    return render(request, 'main/philosophie.html', locals())

def science_and_technology(request):
    news = New.objects.all().order_by('-created_at')[:3]
    user = request.user
    
    teachers = None
    students = None

    if user.is_authenticated:
        print(user.role)
        print(user.username)
        # Recherchez l'utilisateur actuellement connecté en utilisant son ID
        
        teachers = Teacher.objects.filter(user=user)
        students = Student.objects.filter(user=user)
    return render(request, 'main/science_and_technology.html', locals())


def business_administration(request):
    news = New.objects.all().order_by('-created_at')[:3]
    user = request.user
    
    teachers = None
    students = None

    if user.is_authenticated:
        print(user.role)
        print(user.username)
        # Recherchez l'utilisateur actuellement connecté en utilisant son ID
        
        teachers = Teacher.objects.filter(user=user)
        students = Student.objects.filter(user=user)
    return render(request, 'main/business_administration.html', locals())


def social_sciences_and_management(request):
    news = New.objects.all().order_by('-created_at')[:3]
    user = request.user
    
    teachers = None
    students = None

    if user.is_authenticated:
        print(user.role)
        print(user.username)
        # Recherchez l'utilisateur actuellement connecté en utilisant son ID
        
        teachers = Teacher.objects.filter(user=user)
        students = Student.objects.filter(user=user)
    return render(request, 'main/social_sciences_and_management.html', locals())
    
    

def the_registration(request):
    news = New.objects.all().order_by('-created_at')[:3]
    user = request.user
    
    teachers = None
    students = None

    if user.is_authenticated:
        print(user.role)
        print(user.username)
        # Recherchez l'utilisateur actuellement connecté en utilisant son ID
        
        teachers = Teacher.objects.filter(user=user)
        students = Student.objects.filter(user=user)
    return render(request, 'main/the_registration.html', locals())

def about(request):
    news = New.objects.all().order_by('-created_at')[:3]
    user = request.user
    
    teachers = None
    students = None

    if user.is_authenticated:
        print(user.role)
        print(user.username)
        # Recherchez l'utilisateur actuellement connecté en utilisant son ID
        
        teachers = Teacher.objects.filter(user=user)
        students = Student.objects.filter(user=user)
    return render(request, 'main/about.html', locals())


def all_courses_list(request):
    courses = Course.objects.filter(is_deleted=False)
    news = New.objects.all().order_by('-created_at')[:3]
    user = request.user

    philosopie = courses.filter(faculty='Philosophie')
    ingenierie = courses.filter(faculty='Faculté des Sciences et Technologies')
    agronomiques_et_veterinaires = courses.filter(faculty='Agronomiques et Vetérinaires')
    Business_administration =  courses.filter(faculty='Administration des Affaires - Business school')
    social_sciences_and_management = courses.filter(faculty='Sciences Sociales et gestion')
    
    
    teachers = None
    students = None

    if user.is_authenticated:
        print(user.role)
        print(user.username)
        # Recherchez l'utilisateur actuellement connecté en utilisant son ID
        
        teachers = Teacher.objects.filter(user=user)
        students = Student.objects.filter(user=user)

     
    return render(request, 'main/courses.html', locals())   


def alumnis(request):
    alumnis = Alumni.objects.filter(is_deleted=False)
    news = New.objects.all().order_by('-created_at')[:3]
    user = request.user
    
    teachers = None
    students = None

    if user.is_authenticated:
        print(user.role)
        print(user.username)
        # Recherchez l'utilisateur actuellement connecté en utilisant son ID
        
        teachers = Teacher.objects.filter(user=user)
        students = Student.objects.filter(user=user)
    return render(request, 'main/alumnis.html', locals())

    
# Create your views here.
