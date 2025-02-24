from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages

from django.db.models import Q
from students_admin.forms import SouscriptionForm

from userApp.forms import *
from config.countries import COUNTRIES
from main.utils import *
from userApp.models import *
from .models import Level_of_study, Souscription, Student
from main.models import Niveau_d_etude
from university_admin.models import Course


#@login_required
def souscription(request):
    user_set_types = SEX_TYPES
    facultys = Faculty
    level_of_studys = Level_of_study
    COUNTRIES_LIST = COUNTRIES

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        post_name = request.POST.get('post_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        sexe_type = request.POST.get('sexe_type')
        number = request.POST.get('number')
        city = request.POST.get('city')
        adress = request.POST.get('adress')
        common = request.POST.get('common')
        country = request.POST.get('country')
        level_of_study = request.POST.get('level_of_study')
        bithday = request.POST.get('bithday')
        Place_of_birth = request.POST.get('Place_of_birth')
        faculty = request.POST.get('faculty')
        avatar = request.FILES.get('avatar')
        document_file = request.FILES.get('document_file')
        tuteur_name = request.POST.get('tuteur_name')
        tuteur_number = request.POST.get('tuteur_number')
        tuteur_email = request.POST.get('tuteur_email')

        # Vérification des champs obligatoires
        if not first_name or not last_name or not email or not sexe_type or not faculty or not level_of_study:
            messages.error(request, "Veuillez remplir tous les champs obligatoires.")
            return redirect('student_souscription')

        # Création de l'instance
        try:
            souscrip = Souscription.objects.create(
                first_name=first_name,
                post_name=post_name,
                last_name=last_name,
                email=email,
                sexe_type=sexe_type,
                number=number,
                city=city,
                adress=adress,
                common=common,
                country=country,
                level_of_study=level_of_study,
                bithday=bithday,
                Place_of_birth=Place_of_birth,
                faculty=faculty,
                avatar=avatar,
                document_file=document_file,
                tuteur_name=tuteur_name,
                tuteur_number=tuteur_number,
                tuteur_email=tuteur_email
            )
            messages.success(request, "Votre souscription a bien été enregistrée.")
            return redirect('student_souscription')
        except Exception as e:
            messages.error(request, f"Une erreur s'est produite : {str(e)}")

    return render(request, 'students_admin/souscription.html', locals())


@login_required
def  student_admin(request,student_slug=None):
    user = request.user
    student= Student.objects.get(user=user)
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


@login_required
def course_list(request):
    # 1. Récupérez l'utilisateur connecté et l'objet Student associé.
    user = request.user
    student = Student.objects.filter(user=user).first()
    print(Student.objects.filter(user=user))
    print(student)

    if student:
        # 2. Accédez à l'auditoire et à la faculté de l'étudiant.
        auditoire = student.auditoire
        print(auditoire)
        faculty = student.faculty
        print(faculty)

        # 3. Filtrez les cours en fonction de l'auditoire et de la faculté de l'étudiant.
        student_course_lists = Course.objects.filter(auditoire=auditoire, faculty=faculty)

        return render(request, 'students_admin/student_admin.html',locals())

    # Gérez le cas où l'utilisateur n'est pas un étudiant ou n'est pas associé à un étudiant.
    return render(request, 'students_admin/student_course_list.html', {'student_course_lists': []})

@login_required
def edit_profile(request):
    user_set_types = SEX_TYPES
    roles = ROLE
    COUNTRIES_LIST = COUNTRIES
    error = "Champs invalides "
    student= Student.objects.get( user=request.user)
    

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
        if role:
            user.role = role    
        if avatar:
            user.avatarl = avatar
        else:
            user.avatar = '/static/assets/university_mobile_logo_ulc-1 (1).png'                            
        if new_password1 and new_password2:
            if new_password1 != new_password2:
                messages.error(
                    request, 'Les nouveaux mots de passe ne correspondent pas.')
                #return redirect('account')
            user.set_password(new_password1)
            # Empêche la déconnexion de l'utilisateur
            update_session_auth_hash(request, user)

        user.save()

        messages.success(
                request, 'Vos informations ont été mises à jour avec succès.')
        #return redirect('account')
        

    return render(request, 'students_admin/user_profile.html', locals())


def edite_student_profile(request,student_slug=None):
    COUNTRIES_LIST = COUNTRIES
    faculty_list = Faculty


    student= Student.objects.get(user=request.user)

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
        faculty= request.POST.get('faculty')
        auditoire= request.POST.get('auditoire')
        phone = models.CharField(max_length=50)

        if first_name:
            student.first_name = first_name
        if last_name:
            student.last_name = last_name
        if email:
            student.email = email
        if phone:
            student.phone = phone
        if country:
            student.country = country
        if avatar:
            student.avatar = avatar 
        if faculty:
            student.faculty = faculty
        if auditoire:
            student.auditoire = auditoire
        if sexe_type:
            student.sexe_type = sexe_type
        if born_date:
            student.born_date = born_date
        student.save()

        messages.success(
            request, 'Vos informations ont été mises à jour avec succès. '
        )
    return render(request, 'students_admin/student_profile.html', locals())                                           



      




""" def course_list(request):
    user = request.user
    student=Student.objects.filter(user=user)
    auditoires = Niveau_d_etude.objects.filter(faculty=student.faculty)
    student_course_lists=Course.objects.filter(faculty=student.faculty)

    return render(request, 'student_course_list.html', locals())
 """


# Create your views here.
