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

    slug = models.SlugField(unique=True, blank=True, max_length=255, editable=False)  # Non modifiable dans l'admin

    def save(self, *args, **kwargs):
        if not self.slug:  # Générer le slug automatiquement à partir du titre
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

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
