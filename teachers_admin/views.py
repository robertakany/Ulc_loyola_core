from django.shortcuts import render, redirect

from main.models import Auditoire
from teachers_admin.models import Teacher
from university_admin.models import Course

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
from main.utils import *
from django.db.models import Q
from userApp.models import *




"""def add_course(request):
    error = "Il y a une erreur dans ces champs"
    # Obtenir les auditoires disponibles depuis la base de données
    auditoires = Course.objects.all()
    
    # Créer une instance de votre formulaire PdfCourse en passant les auditoires disponibles
    form = CourseForm(auditoires=auditoires)

    teacher = Teacher.objects.get(user=request.user)

    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, auditoires=auditoires)
        if form.is_valid():
            # Utilisez form.cleaned_data pour accéder aux données du formulaire
            cleaned_data = form.cleaned_data
            try:
                courses = Course.objects.create(
                    teacher=teacher,
                    auditoire=cleaned_data['auditoire'],
                    title=cleaned_data['title'],
                    warnings=cleaned_data['warnings'],
                    pdf_files=cleaned_data["pdf_files"]
                )
                courses.save()
                return redirect('courses')
            except Exception as e:
                print('error in courses ')
                return error"""




def teacher_admin(request, teacher_slug):
    user= request.user
    teacher = Teacher.objects.get(user=user, slug=teacher_slug)
    print(teacher.user )
    return render(request, "teachers_admin/teacher_admin_home.html", locals())


def add_course(request):
    error = "Il y a une erreur dans ces champs"
    teacher = Teacher.objects.filter(user=request.user).first()
    print(teacher.user.username)
    if request.method == 'POST':
        print(request.POST)
        image = request.FILES.get('image')
        pdf_files = request.FILES.get('pdf_files')
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        notes = request.POST.get('notes', '')
        auditoires_selected = request.POST.getlist('auditoire')
        try:
            course = Course.objects.create(
                teacher=teacher,
                # auditoire=data.getlist("auditoire"),
                title=title,
                image=image,
                notes=notes,
                pdf_files=pdf_files,
                description=description
            )
            course.auditoire.set(auditoires_selected)
            print("voici le course: ", course)
            # for auditoire_id in auditoires:
            #    course.auditoire.add(auditoire_id)
            return redirect("courses_list")
        except Exception as e:
            print('error in course', e)
            return error
    else:
        auditoires = Auditoire.objects.all()
    return render(request, "teachers_admin/add_course.html", locals())

 



def courses_list(request):
    user = request.user
    teacher = Teacher.objects.filter(user=user).first()
    courses = Course.objects.filter(teacher=teacher)
    return render(request, "teachers_admin/courses.html", locals())



@login_required
def edit_user_profile(request):
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
            return redirect('user_profile_teacher')

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
        

    return render(request, 'teachers_admin/user_profile_teacher.html', locals())

# Create your views here.
