from django.contrib.auth import get_user_model
from django.db import models
from userApp.models import *
from django.utils.text import slugify


#def 'news_images/'(i, filename):
    #return f'news/{i.id}_{i.author.email}/images/{filename}'

class New(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    category = models.CharField(max_length=500, null=True, blank=True)
    views = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User, related_name="user_author", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True , verbose_name='date')
    is_deleted = models.BooleanField(default=False)
    data = models.JSONField(null=True,blank=True)
    image = models.ImageField(
        upload_to='news_images/', null=True, blank=True)
    
    image1 = models.ImageField(null=True, blank=True, upload_to='news_images/')
    image2 = models.ImageField(null=True, blank=True, upload_to='news_images/')
    image3 = models.ImageField(null=True, blank=True, upload_to='news_images/')
    image4 = models.ImageField(null=True, blank=True, upload_to='news_images/')
    image5 = models.ImageField(null=True, blank=True, upload_to='news_images/')
    image6 = models.ImageField(null=True, blank=True, upload_to='news_images/')
    slug = models.SlugField(unique=True, blank=True,max_length=255)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            count = 1
            print(slug)
            while New.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{count}"

                count += 1
            self.slug = slug

                       
        super(New, self).save(*args, **kwargs)

    def add_view(self):
        self.views += 1
        self.save()

    def get_likes_count(self):
        return self.likes.count()

    def get_comments_count(self):
        return self.comments.count()

    def get_views_count(self):
        return self.views
    
    
    @property
    def image_url(self):
        return (self.image and hasattr(self.image, 'url') and self.image.url) or '/static/university_mobile_logo_ulc-1 (1).png'

    @property
    def image1_url(self):
        return (self.image1 and hasattr(self.image1, 'url') and self.image1.url) or '/static/university_mobile_logo_ulc-1 (1).png'

    @property
    def image2_url(self):
        return (self.image2 and hasattr(self.image2, 'url') and self.image2.url) or '/static/university_mobile_logo_ulc-1 (1).png'

    @property
    def image3_url(self):
        return (self.image3 and hasattr(self.image3, 'url') and self.image3.url) or '/static/university_mobile_logo_ulc-1 (1).png'

    @property
    def image4_url(self):
        return (self.image4 and hasattr(self.image4, 'url') and self.image4.url) or '/static/university_mobile_logo_ulc-1 (1).png'

    @property
    def image5_url(self):
        return (self.image5 and hasattr(self.image5, 'url') and self.image5.url) or '/static/university_mobile_logo_ulc-1 (1).png'

    @property
    def image6_url(self):
        return (self.image6 and hasattr(self.image6, 'url') and self.image6.url) or '/static/university_mobile_logo_ulc-1 (1).png'


User = get_user_model()


class Comment(models.Model):
    news = models.ForeignKey(
        New, on_delete=models.CASCADE, related_name='comments'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)


#  likes = models.ManyToManyField(User, related_name='photo_like')#
# def number_of_likes(self):
# return self.like.count()


class Like(models.Model):
    news = models.ForeignKey(
        New, on_delete=models.CASCADE, related_name='likes'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    # Nouveau champ pour indiquer si le like est actif ou non
    is_active = models.BooleanField(default=True)

# Create your models here.
