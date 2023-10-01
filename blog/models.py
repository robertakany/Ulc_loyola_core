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
            base_slug = slugify(self.title)
            slug = base_slug
            count = 1
            while News.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{count}"

                count += 1
            self.slug = slug

        if not self.featured_image:
            self.featured_image = '/static/assets/images/blog/grid/pic2.png'

        super(News, self).save(*args, **kwargs)

# Create your models here.
