from django.shortcuts import render


def home(request):
	return render(request, 'main/home.html')

def home1(request):
	return  render(request, 'main/home1.html')
# Create your views here.
