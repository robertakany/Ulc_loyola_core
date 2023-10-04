from django.db import models
from django.utils.text import slugify

from userApp.models import User
from students_admin.models import Student
from university_admin.models import Course

class Auditoire(models.Model):
    niveau_name = models.CharField(max_length=50, blank=True)
    teachers = models.ManyToManyField('teachers_admin.Teacher', blank=True, related_name='auditoire_teachers')
    course = models.ManyToManyField('university_admin.Course', related_name='auditoire_courses', blank=True)
    data = models.JSONField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.niveau_name)
            slug = base_slug
            count = 1
            while Auditoire.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{count}"

                count += 1
            self.slug = slug

        super(Auditoire, self).save(*args, **kwargs)


# Create your models here.
