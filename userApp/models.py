import django.contrib.auth.models
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

#from students_admin.models import *
#from teachers_admin.models import *

SEX_TYPES = (
    ('M', 'M'),
    ('F', 'F'))

ROLE = (
    ('professeur', 'professeur'),
    ('etudiant', 'etudiant'),
    
)


def user_path(i, filename):
    return f'users/{i.id}_{i.email}/images/{filename}'
class User(django.contrib.auth.models.AbstractUser):
    username= models.CharField(max_length=20 , verbose_name="Nom d'utilisateur")

    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to=user_path, null=True, blank=True,default='users/university_mobile_logo_ulc-1 (1).png')
    country = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)
    sexe_type = models.CharField(max_length=23, choices=SEX_TYPES, default='Male')
    is_delete = models.BooleanField(null=True, blank=True, default=False)
    born_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=70, null=True, blank=True)
    role = models.CharField(max_length=100, choices=ROLE)
    slug = models.SlugField(unique=True, blank=True)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.username} ({self.email})'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.first_name, self.last_name)  
        super().save(*args, **kwargs)
        
    def avatar_url(self):
        return (self.avatar and hasattr(self.avatar, 'url') and self.avatar.url) or 'users/university_mobile_logo_ulc-1 (1).png'
    
@receiver(post_save, sender='students_admin.Student')
def set_user_is_student(sender, instance, **kwargs):
    # Lorsqu'un objet Student est sauvegardé, cette fonction sera appelée.
    # Nous allons définir is_student à True pour l'utilisateur associé.
    if instance.user:
        instance.user.is_student = True
        instance.user.save()

@receiver(post_save, sender='teachers_admin.Teacher')
def set_user_is_student(sender, instance, **kwargs):
    # Lorsqu'un objet Student est sauvegardé, cette fonction sera appelée.
    # Nous allons définir is_student à True pour l'utilisateur associé.
    if instance.user:
        instance.user.is_teacher = True
        instance.user.save()        

@receiver(post_save, sender=User)
def set_user_roles(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'professeur':
            instance.is_teacher = True
        elif instance.role == 'etudiant':
            instance.is_student = True
        instance.save()
                


class Alumni(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    diploma = models.CharField(max_length=255)
    diploma_year = models.IntegerField()
