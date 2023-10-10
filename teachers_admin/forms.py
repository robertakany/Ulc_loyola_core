from django import forms
from university_admin.models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = ('is_deleted','slug','data', 'view',)
        widgets = {
            'faculty': forms.Select(),
            
            'teacher': forms.HiddenInput()
        }
