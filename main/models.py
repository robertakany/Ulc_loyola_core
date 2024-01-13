from django.db import models
from django.utils.text import slugify

from userApp.models import User
from main.utils import Faculty

class Niveau_d_etude(models.Model):
    niveau_name = models.CharField(max_length=50, blank=True)
    teachers = models.ManyToManyField('teachers_admin.Teacher', blank=True, related_name='auditoire_teachers')
    courses = models.ManyToManyField('university_admin.Course', related_name='auditoire_courses', blank=True)
    faculty = models.CharField(max_length=50, choices=Faculty)
    data = models.JSONField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return f'{self.niveau_name} ({self.faculty})'

    """ def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.niveau_name)
            slug = base_slug
            count = 1
            while Niveau_d_etude.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{count}"

                count += 1
            self.slug = slug

        super(Niveau_d_etude, self).save(*args, **kwargs)

    def __str__(self):
        return f'Niveau_d_etude {self.niveau_name}' """
 
class Faculty(models.Model):
    name = models.CharField(max_length=100, choices=Faculty)
 
# Create your models here.
