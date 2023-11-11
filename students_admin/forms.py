from django.forms import ModelForm

from students_admin.models import Souscription


class SouscriptionForm(ModelForm):
    class Meta:
        model=Souscription
        exclude = ['data','amount']
    