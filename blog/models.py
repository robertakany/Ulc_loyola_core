from django.contrib.auth import get_user_model
from django.db import models
from userApp.models import *
from django.utils.text import slugify


#def 'news_images/'(i, filename):
    #return f'news/{i.id}_{i.author.email}/images/{filename}'

class New(models.Model):
    title = models.CharField(max_length=500, verbose_name="Titre")
    sub_title = models.CharField(max_length=500, blank=True, null=True, verbose_name="Sous-titre")
    content = models.TextField(verbose_name="Contenu")
    category = models.CharField(max_length=500, null=True, blank=True, verbose_name="Catégorie")
    views = models.PositiveIntegerField(default=0, editable=False)  # Non modifiable dans l'admin
    author = models.ForeignKey(User, related_name="user_author", on_delete=models.CASCADE, verbose_name="Auteur")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    is_deleted = models.BooleanField(default=False, verbose_name="Supprimé ?")
    data = models.JSONField(null=True, blank=True, verbose_name="Données supplémentaires")

    image = models.ImageField(upload_to='news_images/', null=True, blank=True, verbose_name="Image principale")
    image1 = models.ImageField(upload_to='news_images/', null=True, blank=True, verbose_name="Image 1")
    image2 = models.ImageField(upload_to='news_images/', null=True, blank=True, verbose_name="Image 2")
    image3 = models.ImageField(upload_to='news_images/', null=True, blank=True, verbose_name="Image 3")
    image4 = models.ImageField(upload_to='news_images/', null=True, blank=True, verbose_name="Image 4")
    image5 = models.ImageField(upload_to='news_images/', null=True, blank=True, verbose_name="Image 5")
    image6 = models.ImageField(upload_to='news_images/', null=True, blank=True, verbose_name="Image 6")

    video = models.FileField(upload_to='news_videos/', null=True, blank=True, verbose_name="Vidéo")
    video_url = models.URLField(null=True, blank=True, help_text="Lien YouTube ou Vimeo", verbose_name="URL de la vidéo")

    slug = models.SlugField(unique=True, blank=True, max_length=255)  # Non modifiable dans l'admin

    def __str__(self):
        return self.title  # Afficher le titre dans l'admin

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"


    def get_video_embed_url(self):
        """Convertir une URL YouTube en embed URL"""
        if self.video_url and "youtube.com" in self.video_url:
            return self.video_url.replace("watch?v=", "embed/")
        elif self.video_url and "vimeo.com" in self.video_url:
            return f"https://player.vimeo.com/video/{self.video_url.split('/')[-1]}"
        return None


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
