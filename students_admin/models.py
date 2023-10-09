from django.db import models
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from main.utils import Faculty
from django.db.models.signals import post_save
from django.dispatch import receiver
from userApp.models import *

SEX_TYPES = (
	('M', 'M'),
	('F', 'F'))

ROLE = (
	('professeur', 'professeur'),
	('etudiant', 'etudiant'),

)

Option = (
	('Philosophe','philosophie'),
	('ingeniérie','ingeniérie'),
	('Agronomiques et Vetérinaires', 'Agronomiques et Vetérinaires')
)


def student_path(i, filename):
	return f'student/{i.pk}_{i.email}/images/{filename}'


class Student(models.Model):
	username = models.CharField(max_length=20 , verbose_name="Nom d'utilisateur")
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	user = models.OneToOneField('userApp.User', related_name="student", on_delete=models.SET_NULL, null=True,blank=True)
	year_of_added = models.CharField(max_length=255, null=True, blank=True)
	faculty = models.CharField(max_length=255, choices=Faculty)
	auditoire = models.ForeignKey('main.Auditoire', related_name='auditoire_students', on_delete=models.SET_NULL, blank=True,null=True)
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
	slug = models.SlugField(unique=True, blank=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			base_slug = slugify(self.first_name, self.last_name)
			slug = base_slug
			count = 1
			while Student.objects.filter(slug=slug).exists():
				slug = f"{base_slug}-{count}"

				count += 1
			self.slug = slug


		super(Student, self).save(*args, **kwargs)
@receiver(post_save, sender=Student)
def create_user_for_student(sender, instance, created, **kwargs):
    if created:
        # Créez un objet User associé au Student
        user = User.objects.create(
			first_name=instance.first_name,
			last_name=instance.last_name,
			username=instance.username,
            email=instance.email,
            phone=instance.phone,
            avatar=instance.avatar,
            country=instance.country,
            date_joined=instance.date_joined,
            sexe_type=instance.sexe_type,
            is_delete=instance.is_delete,
            born_date=instance.born_date,
            address=instance.address,
			slug=instance.slug,
            role='etudiant',  # Vous pouvez définir le rôle ici
            is_student=True,  # Assurez-vous que le champ is_student est défini à True
			 
        )
        user.set_password('UlcLoyola1') 
        # Associez le nouvel utilisateur au Student
        instance.user = user
        instance.save()



class StudentCourses(models.Model):
	student = models.ForeignKey(Student, verbose_name="studentOfCourse", on_delete=models.CASCADE)
	courses = models.ForeignKey("university_admin.Course", related_name="courses", on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)

# Create your models here.
