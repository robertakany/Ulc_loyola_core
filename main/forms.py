
# forms.py
from django import forms
from .models import Auditoire

class AuditoireForm(forms.ModelForm):
    class Meta:
        model = Auditoire
        fields = ['niveau_name', 'teachers', 'course']
