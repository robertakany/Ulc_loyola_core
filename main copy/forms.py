
# forms.py
from django import forms
from .models import Niveau_d_etude

class Niveau_d_etudeForm(forms.ModelForm):
    class Meta:
        model = Niveau_d_etude
        fields = ['niveau_name', 'teachers', 'course']
