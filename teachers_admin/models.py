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
    first_name = models.CharField(max_length=45, null=True, blank=True)
    last_name = models.CharField(max_length=45, null=True, blank=True)
    username = models.CharField(max_length=20, null=True, blank=True, verbose_name="Nom d'utilisateur")
    email = models.EmailField(_('email address'), unique=True, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    sexe_type = models.CharField(max_length=23, choices=SEX_TYPES, default='Male')
    is_delete = models.BooleanField(null=True, blank=True, default=False)
    born_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=70, null=True, blank=True)
    courses = models.CharField(max_length=50, null=True, blank=True)
    data = models.JSONField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)


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
        
""" @receiver(post_save, sender=Teacher)
def create_user_for_teacher(sender, instance, created, **kwargs):
    if created:
        # Créez un objet User associé au Teacher
        user = User.objects.create(
            first_name=instance.first_name,
            last_name=instance.last_name,
            username=instance.username,
            email=instance.email,
            phone=instance.phone,
            country=instance.country,
            sexe_type=instance.sexe_type,
            is_delete=instance.is_delete,
            born_date=instance.born_date,
            address=instance.address,
            slug=instance.slug,
            role='professeur',  # Vous pouvez définir le rôle ici,
            is_teacher=True,  # Assurez-vous que le champ is_teacher est défini à True
            #
        )
        # Définissez le mot de passe par défaut pour l'utilisateur
        user.set_password('UlcLoyola1') 
        # Associez le nouvel utilisateur au Teacher
        instance.user = user
        instance.save() """

# Create your models here.