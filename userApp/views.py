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
from students_admin.models import Student
from teachers_admin.models import Teacher
from datetime import datetime

from django.db.models import Q


def connect(request):
    form = LoginForm()
    error = ''
    next = request.GET.get('next')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        print('-----------LOGIN-----------')
        print(form)
        if form.is_valid():
            username_or_email = form.cleaned_data['username_or_email']
            password = form.cleaned_data['password']
            # Recherche de l'utilisateur par email ou nom d'utilisateur
            user = User.objects.filter(
                Q(email=username_or_email) | Q(username=username_or_email)
            ).first()
            print(user)
            if user is not None and user.check_password(password):
                login(request, user)
                print('_________OK_____________')
                response = redirect(next or 'home')
                return response
            else:
                print('_________NONE________')
        else:
            error = 'Identifiants invalides'
    return render(request, 'user/login_page.html', {'form': form, 'error': error, 'next': next})

def disconnect(request):
    logout(request)
    response= redirect('home')
    return response

def signup(request):
    user_set_types = SEX_TYPES
    roles = ROLE

    COUNTRIES_LIST = COUNTRIES

    form = SignupForm()
    errors = ''
    next = request.GET.get('next')

    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        try:
            if form.is_valid():
            
                print('_________beatiful God is_______')
                user = form.save()
                print('this is the save user',user)
                if user:
                    login(request, user)
                    print('this is the user login', user)
                 
                    response = redirect('home')
                    print(user)
                    return response
            else:
                errors = 'Champs invalides'
        except Exception as e:
                print('error',e)        
    return render(request, 'user/signup.html', locals())




@login_required
def edit_profile(request):

    COUNTRIES_LIST = COUNTRIES
    

    if request.method == 'POST':
        user = request.user
        # Récupération des données du formulaire
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        country = request.POST.get('country')
        old_password = request.POST.get('old_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')

        # Vérification de l'ancien mot de passe
        if old_password and not user.check_password(old_password):
            messages.error(request, 'Le mot de passe actuel est incorrect.')
            return redirect('account')

        # Mise à jour des données de l'utilisateur
        if first_name:
            user.first_name = first_name
        if last_name:
            user.lasst_name = last_name
        if country:
            user.country = country
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

    return render(request, 'user/user_profil.html', locals())



@login_required(login_url='login')
def upload_profile_photo(request):
    user = request.user
    form = UploadProfilePhotoForm(instance=request.user)
    if request.method == 'POST':
        form = UploadProfilePhotoForm(
            request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            #return redirect('account')

    return render(request, 'user/upload_profile_photo.html', {
        'form': form
    })


def password(request):
    return render(request, 'user/password.html')


def deconnexion(request):
    logout(request)
    return redirect('home')
# Create your views here.

""" def edit_password(request):
    teacher = Teacher.objects.get(user=request.user)
    student = Student.objects.get(user=request.user)

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

@login_required
def edit_user_profile(request):
    user_set_types = SEX_TYPES
    roles = ROLE
    COUNTRIES_LIST = COUNTRIES
    error = "Champs invalides "
    if request.method == 'POST':
        if 'verification' in request.POST:
        # Handle form submission and update the user's profile
            user = request.user
            user.username = request.POST['username']
            user.last_name = request.POST['last_name']
            user.first_name = request.POST['first_name']
            user.email = request.POST['email']
            user.role = request.POST['role']
            user.country = request.POST.get('country')
            user.phone = request.POST.get('phone')
            user.address = request.POST.get('address')
            born_date = request.POST.get('born_date')
            if born_date:
                try:
                    born_date = datetime.strptime(born_date, '%Y-%m-%d').date()
                except ValueError:
                    messages.error(request, 'Format de date de naissance invalide. Utilisez AAAA-MM-JJ.')
                    print(messages)
                    return redirect('modifier_profil')

                user.born_date = born_date

            # Handle avatar upload if a new file is selected
            if 'avatar' in request.FILES:
                user.avatar = request.FILES.get('avatar')

            user.save()
            success = True
            
                    
            messages.success(request, 'Profile updated successfully')
            return redirect('user_profile_edit')  # Redirect to the user's profile page or any other desired page
        else:
        
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
                    password_error=True
                    password_error=False
                    #return redirect('account')
                user.set_password(new_password1)
                password_success=True
                password_error=False
                # Empêche la déconnexion de l'utilisateur
                update_session_auth_hash(request, user)

            user.save()
            messages.success(
                    request, 'Vos informations ont été mises à jour avec succès.')
            print(messages)            
    return render(request, 'user/edit_user_profile.html', locals())
