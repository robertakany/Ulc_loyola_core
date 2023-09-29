from django import forms

from blog.models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        exclude = ['data', 'is_deleted', 'author', 'views']
