from django.db import models
from django.utils.text import slugify
from university_admin.models import Course
from django.utils.translation import gettext_lazy as _
from userApp.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



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

class Teacher(models.Model):
    user = models.OneToOneField('userApp.User', related_name="user_teacher", on_delete=models.CASCADE , null=False, blank=False)
    first_name = models.CharField(max_length=45, null=True, blank=True, verbose_name='Prenom')
    last_name = models.CharField(max_length=45, null=True, blank=True,verbose_name='Nom')
    username = models.CharField(max_length=20, null=True, blank=True, verbose_name="Nom d'utilisateur")
    email = models.EmailField(_('email address'), unique=True, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    sexe_type = models.CharField(max_length=23, choices=SEX_TYPES, default='Male',verbose_name='Sexe')
    born_date = models.DateField(null=True, blank=True,verbose_name="Date d'anniversaire")
    address = models.CharField(max_length=70, null=True, blank=True)
    courses = models.CharField(max_length=50, null=True, blank=True,verbose_name='Cours')
    data = models.JSONField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)
    is_delete = models.BooleanField(null=True, blank=True, default=False)
    class Meta:
        verbose_name = "Professeur"  
        verbose_name_plural = "Professeurs"
        


    def save(self, *args, **kwargs):
        if self.user:
            self.username = self.user.username
            self.first_name = self.user.first_name
            self.last_name = self.user.last_name
            self.email = self.user.email
            self.phone = self.user.phone
            self.country = self.user.country
            self.address = self.user.address
            self.sexe_type = self.user.sexe_type
            self.born_date = self.user.born_date

        if not self.slug:
            base_slug = slugify(self.first_name, self.last_name)
            slug = base_slug
            count = 1
            while Teacher.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{count}"

                count += 1
            self.slug = slug
        super(Teacher, self).save(*args, **kwargs)
        
        
    def __str__(self):
        return f'Professeur {self.first_name} {self.last_name} {self.username}'
        

# Create your models here.