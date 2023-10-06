from students_admin.models import Student
from main.models import Auditoire
from university_admin.models import Course
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from userApp.forms import *
from userApp.models import User
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages
from config.countries import COUNTRIES

from django.db.models import Q
from userApp.models import *



def  student_admin(request,student_slug):
    user = request.user
    student= Student.objects.get(user=user,slug=student_slug)
    if student:
        # 2. Accédez à l'auditoire et à la faculté de l'étudiant.
        auditoire = student.auditoire
        print(auditoire)
        faculty = student.faculty
        print(faculty)

        # 3. Filtrez les cours en fonction de l'auditoire et de la faculté de l'étudiant.
        student_course_lists = Course.objects.filter(auditoire=auditoire, faculty=faculty)

    print(student_slug, student.user)
    return render(request, 'students_admin/student_admin.html',locals())


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

@login_required
def edit_profile(request):
    user_set_types = SEX_TYPES
    roles = ROLE
    COUNTRIES_LIST = COUNTRIES

    if request.method == 'POST':
        user = request.user
        # Récupération des données du formulaire
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        country = request.POST.get('country')
        phone = request.POST.get('phone')
        avatar = request.FILES.get('avatar')
        email = request.POST.get('email')
        sexe_type = request.POST.get('sexe_type')
        born_date = request.POST.get('born_date')
        role=request.POST.get('role')
        address = request.POST.get('address')
        old_password = request.POST.get('old_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')

        # Vérification de l'ancien mot de passe
        if old_password and not user.check_password(old_password):
            messages.error(request, 'Le mot de passe actuel est incorrect.')
            return redirect('user_profile')

        # Mise à jour des données de l'utilisateur
        if first_name:
            user.first_name = first_name
        if last_name:
            user.lasst_name = last_name
        if country:
            user.country = country
        if phone:
            user.phone = phone
        if email:
            user.email = email
        if sexe_type:
            user.sexe_type = sexe_type
        if born_date:
            user.born_date = born_date
        if address:
            user.address = address
        if avatar:
            user.avatar.url = avatar
        else:
            user.avatar.url = '/static/assets/university_mobile_logo_ulc-1 (1).png'                            
        if new_password1 and new_password2:
            if new_password1 != new_password2:
                messages.error(
                    request, 'Les nouveaux mots de passe ne correspondent pas.')
                return redirect('account')
            user.set_password(new_password1)
            # Empêche la déconnexion de l'utilisateur
            update_session_auth_hash(request, user)

        user.save()

        messages.success(
            request, 'Vos informations ont été mises à jour avec succès.')
        #return redirect('account')

    return render(request, 'students_admin/user_profile.html', locals())




""" def course_list(request):
    user = request.user
    student=Student.objects.filter(user=user)
    auditoires = Auditoire.objects.filter(faculty=student.faculty)
    student_course_lists=Course.objects.filter(faculty=student.faculty)

    return render(request, 'student_course_list.html', locals())
 """


# Create your views here.
