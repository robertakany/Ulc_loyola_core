from django.db import models
from userApp.models import User
from students_admin.models import Student
from university_admin.models import PdfCourse

class Audience(models.Model):
    niveau_name = models.CharField(max_length=50, blank=True)
    teachers = models.ManyToManyField('teachers_admin.Teacher', blank=True ,null=True , related_name='audience_teachers')
    course = models.ManyToManyField('university_admin.PdfCourse', related_name='audience_courses', blank=True)
    data = models.JSONField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)


# Create your models here.
