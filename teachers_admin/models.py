from django.db import models
from django.utils.text import slugify

from userApp.models import User  # Import correct
from university_admin.models import Course


class Teacher(models.Model):
    user = models.OneToOneField(User, related_name="user_teacher", on_delete=models.CASCADE)
    #courses = models.CharField(max_length=50, null=True, blank=True)
    year_of_experience = models.CharField(max_length=255, null=True, blank=True)
    year_of_added = models.CharField(max_length=255, null=True, blank=True)
    data = models.JSONField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.user.username)
            slug = base_slug
            count = 1
            while Teacher.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{count}"

                count += 1
            self.slug = slug
        super(Teacher, self).save(*args, **kwargs)
# Create your models here.