from django.db import models
from userApp.models import User  # Import correct
from university_admin.models import PdfCourse


class Teacher(models.Model):
    user = models.OneToOneField(User, related_name="user_teacher", on_delete=models.CASCADE)
    courses = models.CharField(max_length=50, null=True, blank=True)
    year_of_experience = models.CharField(max_length=255, null=True, blank=True)
    year_of_added = models.CharField(max_length=255, null=True, blank=True)
    data = models.JSONField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

# Create your models here.