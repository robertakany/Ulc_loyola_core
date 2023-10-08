from django.shortcuts import render

from students_admin.models import Student
from teachers_admin.models import Teacher
from userApp import User


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
    user = request.user
    
    teachers = None
    students = None

    if user.is_authenticated:
        print(user.role)
        print(user.username)
        # Recherchez l'utilisateur actuellement connecté en utilisant son ID
        
        teachers = Teacher.objects.filter(user=user)
        students = Student.objects.filter(user=user)

    return render(request, 'main/home.html', {
        'user': user,
        'teachers': teachers,
        'students': students,
    })


def home1(request):
	return  render(request, 'main/home1.html')
# Create your views here.
