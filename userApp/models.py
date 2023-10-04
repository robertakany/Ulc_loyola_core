import django.contrib.auth.models
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

SEX_TYPES = (
    ('M', 'M'),
    ('F', 'F'))

ROLE = (
    ('professeur', 'professeur'),
    ('etudiant', 'etudiant'),
    
)


def user_path(i, filename):
    return f'users/{i.pk}_{i.email}/images/{filename}'
class User(django.contrib.auth.models.AbstractUser):
    # username= models.CharField(max_length=20 , verbose_name="Nom d'utilisateur")

    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to=user_path, null=True, blank=True)
    country = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)
    sexe_type = models.CharField(max_length=23, choices=SEX_TYPES, default='Male')
    is_delete = models.BooleanField(null=True, blank=True, default=False)
    born_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=70, null=True, blank=True)
   # role = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.username} ({self.email})'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username, self.last_name)
        if not self.avatar.url or self.avatar:
            self.avatar = '/static/assets/university_mobile_logo_ulc-1 (1).png'    
        super().save(*args, **kwargs)
        
    def avatar_url(self):
        return (self.avatar and hasattr(self.avatar, 'url') and self.avatar.url) or '/static/assets/university_mobile_logo_ulc-1 (1).png'



class Alumni(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    diploma = models.CharField(max_length=255)
    diploma_year = models.IntegerField()
