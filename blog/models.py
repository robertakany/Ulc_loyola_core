from django.contrib.auth import get_user_model
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
    data = models.JSONField(null=True,blank=True)
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
            self.featured_image = 'static/assets/images/80_863_49206349206x566_66666666667_1251485546_1466675589diplomes-africains-0.jpg'

        super(News, self).save(*args, **kwargs)

    def add_view(self):
        self.views += 1
        self.save()

    def get_likes_count(self):
        return self.likes.count()

    def get_comments_count(self):
        return self.comments.count()

    def get_views_count(self):
        return self.views


User = get_user_model()


class Comment(models.Model):
    news = models.ForeignKey(
        News, on_delete=models.CASCADE, related_name='comments'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)


#  likes = models.ManyToManyField(User, related_name='photo_like')#
# def number_of_likes(self):
# return self.like.count()


class Like(models.Model):
    news = models.ForeignKey(
        News, on_delete=models.CASCADE, related_name='likes'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    # Nouveau champ pour indiquer si le like est actif ou non
    is_active = models.BooleanField(default=True)

# Create your models here.
