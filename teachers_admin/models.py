from django.db import models
from django.utils.text import slugify
from university_admin.models import Course
from django.utils.translation import gettext_lazy as _
from userApp.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver



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

class Teacher(models.Model):
    user = models.OneToOneField('userApp.User', related_name="user_teacher", on_delete=models.SET_NULL , null=True, blank=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    username = models.CharField(max_length=20 , verbose_name="Nom d'utilisateur")
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    sexe_type = models.CharField(max_length=23, choices=SEX_TYPES, default='Male')
    is_delete = models.BooleanField(null=True, blank=True, default=False)
    born_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=70, null=True, blank=True)
    courses = models.CharField(max_length=50, null=True, blank=True)
    #year_of_added = models.CharField(max_length=255, null=True, blank=True)
    data = models.JSONField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.user.first_name

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.first_name, self.last_name)
            slug = base_slug
            count = 1
            while Teacher.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{count}"

                count += 1
            self.slug = slug
        super(Teacher, self).save(*args, **kwargs)
@receiver(post_save, sender=Teacher)
def create_user_for_teacher(sender, instance, created, **kwargs):
    if created:
        # Créez un objet User associé au Teacher
        user = User.objects.create(
            username=instance.username,
            email=instance.email,
            phone=instance.phone,
            country=instance.country,
            sexe_type=instance.sexe_type,
            is_delete=instance.is_delete,
            born_date=instance.born_date,
            address=instance.address,
            role='professeur',  # Vous pouvez définir le rôle ici,
            is_teacher=True,  # Assurez-vous que le champ is_teacher est défini à True
        )

        # Associez le nouvel utilisateur au Teacher
        instance.user = user
        instance.save()

# Create your models here.