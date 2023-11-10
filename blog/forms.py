from django import forms

from blog.models import New


class NewForm(forms.ModelForm):
    class Meta:
        model = New
        exclude = ['data', 'is_deleted', 'author', 'views']
