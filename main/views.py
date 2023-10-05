from django.shortcuts import render

from students_admin.models import Student
from teachers_admin.models import Teacher
from userApp import User


def home(request):
	user=request.user
	
	teachers = Teacher.objects.filter(user=user)
	students = Student.objects.filter(user=user)
	return render(request, 'main/home.html',locals())

def home1(request):
	return  render(request, 'main/home1.html')
# Create your views here.
