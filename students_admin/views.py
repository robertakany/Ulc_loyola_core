from django.shortcuts import render
from students_admin.models import Student
from main.models import Auditoire
from university_admin.models import Course




def course_list(request):
    # 1. Récupérez l'utilisateur connecté et l'objet Student associé.
    user = request.user
    student = Student.objects.filter(user=user).first()
    print(student)

    if student:
        # 2. Accédez à l'auditoire et à la faculté de l'étudiant.
        auditoire = student.auditoire
        print(auditoire)
        faculty = student.faculty
        print(faculty)

        # 3. Filtrez les cours en fonction de l'auditoire et de la faculté de l'étudiant.
        student_course_lists = Course.objects.filter(auditoire=auditoire, faculty=faculty)

        return render(request, 'students_admin/student_course_list.html', locals())

    # Gérez le cas où l'utilisateur n'est pas un étudiant ou n'est pas associé à un étudiant.
    return render(request, 'students_admin/student_course_list.html', {'student_course_lists': []})



""" def course_list(request):
    user = request.user
    student=Student.objects.filter(user=user)
    auditoires = Auditoire.objects.filter(faculty=student.faculty)
    student_course_lists=Course.objects.filter(faculty=student.faculty)

    return render(request, 'student_course_list.html', locals())
 """


# Create your views here.
