from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from userApp.models  import *



class LoginForm(forms.Form):
    username_or_email = forms.CharField(max_length=50)
    password = forms.CharField(
        max_length=50, label="Mot de passe", widget=forms.PasswordInput(attrs={'class': 'password-input'}))


class SignupForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username','first_name','last_name','email', 'phone', 'country','password1', 'password2', 'avatar','born_date','sexe_type','address',)
        
        def save(self, commit = True):
            user = super(SignupForm, self).save(commit=False)
            user.username = self.cleaned_data.get("username", None)
            user.first_name = self.cleaned_data.get("first_name", None)
            user.last_name = self.cleaned_data.get("last_name", None)
            user.email = self.cleaned_data.get("email", None),
            #user.avatar = self.cleaned_data.get("avatar", None)
           
            

            if commit:

                user.save()

            return user


       
class UploadProfilePhotoForm(forms.ModelForm):
     class Meta:
         model = User
         fields = ('avatar',)
       