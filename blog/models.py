from django.db import models
from userApp.models import *
from django.utils.text import slugify


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    featured_image = models.ImageField(
        upload_to='news_images/', null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    views = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User, related_name="user_author", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    data = models.JSONField(null=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

        if self.featured_image:
            pass
        else:
            self.featured_image = '/static/assets/images/blog/grid/pic2.png'
        return super(News).save(**kwargs)
# Create your models here.
