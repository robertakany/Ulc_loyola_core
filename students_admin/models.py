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
	('autres', 'autres'),

)

Option = (
	('Philosophe','philosophie'),
	('ingeniérie','ingeniérie'),
	('Agronomiques et Vetérinaires', 'Agronomiques et Vetérinaires')
)

Level_of_study= (
	('Baccalauréat', 'Baccalauréat'),
	('Graduat', 'Graduat'),
	('License', 'License'),
	('Master', 'Master'),
	('Doctorat', 'Doctorat')
	
)


def student_path(i, filename):
	return f'student/{i.pk}_{i.email}/images/{filename}'


class Student(models.Model):
	user = models.OneToOneField('userApp.User', related_name="student", on_delete=models.CASCADE, null=False,blank=False)
	username = models.CharField(max_length=20 , verbose_name="Nom d'utilisateur", null=True, blank=True)
	first_name = models.CharField(max_length=45, null=True, blank=True)
	last_name = models.CharField(max_length=45, null=True, blank=True)
	year_of_added = models.CharField(max_length=255, null=True, blank=True)
	faculty = models.CharField(max_length=255, choices=Faculty)
	auditoire = models.ForeignKey('main.Niveau_d_etude', related_name='auditoire_students', on_delete=models.SET_NULL, blank=True,null=True)
	email = models.EmailField(_('email address'), unique=True, null=True, blank=True)
	phone = models.CharField(max_length=50, null=True, blank=True)
	avatar = models.ImageField(upload_to=student_path, null=True, blank=True)
	date_joined = models.DateTimeField(auto_now_add=True)
	sexe_type = models.CharField(max_length=23, choices=SEX_TYPES, default='Male', blank=True)
	is_delete = models.BooleanField(null=True, blank=True, default=False)
	born_date = models.DateField(null=True, blank=True)
	address = models.CharField(max_length=70, null=True, blank=True)
	country = models.CharField(max_length=100, null=True, blank=True)
	data = models.JSONField(blank=True, null=True)
	slug = models.SlugField(unique=True, blank=True)

	def save(self, *args, **kwargs):
		if self.user:
			self.username = self.user.username
			self.first_name = self.user.first_name
			self.last_name = self.user.last_name
			self.email = self.user.email
			self.phone = self.user.phone
			self.avatar = self.user.avatar
			self.sexe_type = self.user.sexe_type
			self.country = self.user.country
			self.address = self.user.address
			self.born_date = self.user.born_date

		if not self.slug:
			base_slug = slugify(self.first_name, self.last_name)
			slug = base_slug
			count = 1
			while Student.objects.filter(slug=slug).exists():
				slug = f"{base_slug}-{count}"

				count += 1
			self.slug = slug
		super(Student, self).save(*args, **kwargs)
	

	def __str__(self):
		return f'Etudiant {self.first_name} {self.last_name} {self.username}'


class Souscription(models.Model):
    #student = models.ForeignKey(Student, related_name="student_registration", on_delete=models.SET_NULL,
                                #null=True, blank=True)
    first_name = models.CharField(max_length=45, verbose_name='Prenom')
    last_name = models.CharField(max_length=45,verbose_name='Nom de la famille')
    email = models.EmailField(max_length=233, unique=True)
    number = models.CharField(max_length=255, null=True , blank=True)
    adress = models.CharField(max_length=324 ,blank=True, null=True)
    common = models.CharField(max_length=324 ,blank=True, null=True)
    country = models.CharField(max_length=324 ,blank=True, null=True)
    level_of_study = models.CharField(max_length=255, choices=Level_of_study)
    bithday = models.CharField(max_length=345 )
    Place_of_birth=models.CharField(max_length=200, blank=True, null=True)
    #year_of_added = models.CharField(max_length=255, null=True, blank=True)
    faculty = models.CharField(max_length=255, choices=Faculty)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    data = models.JSONField(null=True, blank=True)

""" @receiver(post_save, sender=Student)
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
 """


class StudentCourses(models.Model):
	student = models.ForeignKey(Student, verbose_name="studentOfCourse", on_delete=models.CASCADE)
	courses = models.ForeignKey("university_admin.Course", related_name="courses", on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)

# Create your models here.
