from django.shortcuts import render, redirect

from main.models import Niveau_d_etude
from teachers_admin.models import Teacher
from university_admin.models import Course

from students_admin.models import Student
from main.models import Niveau_d_etude
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
from teachers_admin.forms import CourseForm
from django.shortcuts import render, redirect, get_object_or_404





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




def teacher_admin(request, teacher_slug=None):
    user= request.user
    teacher = Teacher.objects.get(user=user)
    print(teacher.user )
    courses = Course.objects.filter(teacher=teacher)
    return render(request, "teachers_admin/teacher_admin_home.html", locals())


def add_course(request):
    facultys = Faculty
    error = "Il y a une erreur dans ces champs"
    teacher = Teacher.objects.filter(user=request.user).first()
    print(teacher.user.username)
    if request.method == 'POST':
        print(request.POST)
        image = request.FILES.get('image')
        pdf_files = request.FILES.get('pdf_files')
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        auditoires_selected = request.POST.getlist('auditoire')
        faculty = request.POST.get('faculty')
        try:
            course = Course.objects.create(
                teacher=teacher,
                # auditoire=data.getlist("auditoire"),
                title=title,
                image=image,
                faculty=faculty,
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
        auditoires = Niveau_d_etude.objects.all()
    return render(request, "teachers_admin/add_course.html", locals())

 



def courses_list(request):
    user = request.user
    teacher = Teacher.objects.filter(user=user).first()
    courses = Course.objects.filter(teacher=teacher)
    return render(request, "teachers_admin/courses.html", locals())


def course_update(request, course_pk ):
    facultys = Faculty
    error = "Il y a une erreur dans ces champs"
    teacher = Teacher.objects.filter(user=request.user).first()
    try:
        course = get_object_or_404(Course, id=course_pk, teacher=teacher)
    except Course.DoesNotExist:
        # Handle the case where the course doesn't exist or doesn't belong to the teacher
        return redirect("courses_list")  # You can redirect to a suitable URL

    if request.method == 'POST':
        image = request.FILES.get('image')
        pdf_files = request.FILES.get('pdf_files')
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        notes = request.POST.get('notes', '')
        auditoires_selected = request.POST.getlist('auditoire')
        faculty = request.POST.get('faculty')

        # Update the course fields
        course.title = title
        course.image = image
        course.notes = notes
        course.pdf_files = pdf_files
        course.description = description
        course.auditoire.set(auditoires_selected)
        course.faculty = faculty  # Set the faculty field

        course.save()

        return redirect("courses_list")

    auditoires = Niveau_d_etude.objects.all()   
    return render(request, 'teachers_admin/course_update.html', locals())    


""" @login_required
def edit_user_profile(request):
    user_set_types = SEX_TYPES
    roles = ROLE
    COUNTRIES_LIST = COUNTRIES
    error = "Champs invalides "
    teacher= Teacher.objects.get( user=request.user)
    
    
    if request.method == 'POST':
            
        user = request.user
        # Récupération des données du formulaire
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        country = request.POST.get('country')
        phone = request.POST.get('phone')
        avatar = request.FILES.get('avatar')
        email = request.POST.get('email')
        born_date = request.POST.get('born_date')
        role=request.POST.get('role')
        address = request.POST.get('address')

        # Mise à jour des données de l'utilisateur
        if first_name:
            user.first_name = first_name
            print('ok',user.first_name)
            
        else:
            user.first_name = user.first_name
            print('no') 
        if last_name:
            user.last_name = last_name
            print('ok',user.last_name)
        else:
            print('no')
            user.last_name = user.last_name    
        if country:
            user.country = country
            print('ok',user.country)
        else:
            print('no country)',user.country) 
            user.country = user.country   
        if phone:
            user.phone = phone
            print('ok',user.phone)
        else:
            print('no') 
        if email:
            user.email = email
            print('ok',user.email)
        else:
            print('no')  
        if born_date:
            user.born_date = born_date
            print('ok',user.born_date)
        else:
            print('no') 
        if address:
            user.address = address
            print('ok',user.address)
        else:
            print('no') 
        if role:
            user.role = role  
            print('ok',user.role)  
        else:
            print('no') 
        if avatar:
            user.avatarl = avatar
            print('ok',user.avatar)
        else:
            user.avatar = user.avatar                        
        user.save()
        
        messages.success(
                request, 'Vos informations ont été mises à jour avec succès.')
        print(messages)
        #return redirect('account')
   
               

    return render(request, 'teachers_admin/user_profile_teacher.html', locals())

def edit_password(request):
    teacher = Teacher.objects.get(user=request.user)

    if request.method == 'POST':
        try:
            user = request.user
            old_password = request.POST.get('old_password')
            new_password1 = request.POST.get('new_password1')
            new_password2 = request.POST.get('new_password2')
        except Exception as e:
            print('Error',e.message)    

        # Vérification de l'ancien mot de passe
        if old_password and not user.check_password(old_password):
            messages.error(request, 'Le mot de passe actuel est incorrect.')
            return redirect('user_profile_teacher') 
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
        print(messages)

        return render(request, 'userApp/edit_password.html', locals())
 """






        
        
# Create your views here.
