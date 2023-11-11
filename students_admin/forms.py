from django import forms

from students_admin.models import Souscription


class SouscriptionForm(forms.ModelForm):
    model=Souscription
    exclude = ['data',]
    