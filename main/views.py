from django.shortcuts import render
from teachers_admin.models import Teacher
from userApp import User


def home(request):
	user=request.user
	teachers = Teacher.objects.filter(user=user)
	return render(request, 'main/home.html',locals())

def home1(request):
	return  render(request, 'main/home1.html')
# Create your views here.
