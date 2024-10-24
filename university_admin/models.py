from django.db import models
from django.utils.text import slugify

from students_admin.models import Student
from main.utils import Faculty 






class Course(models.Model):
    teacher = models.ForeignKey('teachers_admin.Teacher', on_delete=models.SET_NULL, blank=True, null=True,verbose_name='Professeur')
    auditoire = models.ManyToManyField('main.Niveau_d_etude', related_name="course_auditoire", )
    faculty = models.CharField(max_length=255, choices=Faculty,verbose_name='Faculté')
    title = models.CharField(max_length=255,verbose_name='Titre')
    image = models.ImageField(default='/static/admin/assets/images/logo-mobile.png')
    notes = models.TextField(verbose_name='note', null=True, blank=True)
    pdf_files = models.FileField(upload_to='cours_pdfs/',verbose_name='Fichiers pdf')
    description = models.TextField(null=True, blank=True)
    date_of_register = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100)
    view= models.PositiveIntegerField(default=0)
    data = models.JSONField(null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            count = 1
            while Course.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{count}"

                count += 1
            self.slug = slug

        super(Course, self).save(*args, **kwargs)
    @property
    def image_url(self):
        return (self.image and hasattr(self.image, 'url') and self.image.url) or '/static/assets/university_mobile_logo_ulc-1 (1).png'
    
    def __str__(self):
        return f'Cours: {self.title}'
    
    class Meta:
        verbose_name = "Cours"  
        verbose_name_plural = "Cours"
        

class StudentCourses(models.Model):
    student = models.ForeignKey(Student, related_name="student_courses", on_delete=models.CASCADE)
    courses = models.ForeignKey(Course, on_delete=models.CASCADE)
    auditoire = models.ForeignKey('main.Niveau_d_etude', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Cours d'etudiant"  
        verbose_name_plural = "Cours d'etudiants" 
        


class Alumni(models.Model):
    image = models.ImageField(default='/static/admin/assets/images/logo-mobile.png')
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    diploma = models.CharField(max_length=255, null=True, blank=True)
    diploma_year = models.IntegerField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    
    @property
    def image_url(self):
        return (self.image and hasattr(self.image, 'url') and self.image.url) or '/static/favicon-144x144-1.png'
    
    def __str__(self):
        return f'Alumni: {self.name}'


class TeacherStudentRelation(models.Model):
    Teacher = models.ForeignKey('teachers_admin.Teacher', related_name="teachers", null=True, blank=True,
                                on_delete=models.CASCADE)
    student = models.ForeignKey(Student, null=True, related_name="students", blank=True, on_delete=models.CASCADE)


class CalendrierAcademique(models.Model):
    annee_scolaire = models.CharField(max_length=10)
    date_debut_semestre1 = models.DateField()
    date_fin_semestre1 = models.DateField()
    date_debut_semestre2 = models.DateField()
    date_fin_semestre2 = models.DateField()

    # Ajoutez d'autres champs en fonction de votre calendrier académique


class NewletterEmail(models.Model):
    email = models.EmailField(unique=True)

# Create your models here.
