from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect

from userApp import User
from students_admin.models import Student


# Create (Création d'un étudiant)
def create_student(request):
	if request.method == 'POST':
		data = [request.POST, request.FILES]
		print(data)
		users = User.objects.all()

		for u in users:
			if data['email'] != u.email:
				data['user'] = None
			else:
				data['user'] = user
				user = data[user]
		student = Student.objects.create(
			user = user,
			first_name = data['first_name'],
			last_name = data['last_name'],
			year_of_added = data['year_of_added'],
			option = data['option'],
			class_level = data['class_level'],
			email = data['email'],
			phone = data['phone'],
			country = data['country'],
			sexe_type = data['sexe_type'],
			born_date = data['born_date'],
			address = data['address']
		)

		return redirect('student_list')
	return render(request, 'university_admin/add_student.html', locals())




# Create your views here.
