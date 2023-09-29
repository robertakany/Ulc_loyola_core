from django.db import models
from django.db import models
from userApp.models import User  # Import correct
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

SEX_TYPES = (
	('M', 'M'),
	('F', 'F'))

ROLE = (
	('professeur', 'professeur'),
	('etudiant', 'etudiant'),

)


def student_path(i, filename):
	return f'student/{i.pk}_{i.email}/images/{filename}'


class Student(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	user = models.OneToOneField(User, related_name="student", on_delete=models.SET_NULL, null=True,blank=True)
	year_of_added = models.CharField(max_length=255, null=True, blank=True)
	option = models.CharField(max_length=200)
	class_level = models.CharField(max_length=50, blank=True, null=True, verbose_name="niveau d'étude")
	email = models.EmailField(_('email address'), unique=True)
	phone = models.CharField(max_length=50)
	avatar = models.ImageField(upload_to=student_path, null=True, blank=True)
	country = models.CharField(max_length=100)
	date_joined = models.DateTimeField(auto_now_add=True)
	sexe_type = models.CharField(max_length=23, choices=SEX_TYPES, default='Male')
	is_delete = models.BooleanField(null=True, blank=True, default=False)
	born_date = models.DateField(null=True, blank=True)
	address = models.CharField(max_length=70, null=True, blank=True)
	data = models.JSONField(blank=True, null=True)


class StudentCourses(models.Model):
	student = models.ForeignKey(Student, verbose_name="studentOfCourse", on_delete=models.CASCADE)
	courses = models.ForeignKey("university_admin.PdfCourse", related_name="courses", on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)

# Create your models here.
