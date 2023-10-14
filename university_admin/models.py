from django.db import models
from django.utils.text import slugify

from students_admin.models import Student
from main.utils import Faculty 





class Registration(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    user = models.OneToOneField('userApp.User', related_name="student_registration", on_delete=models.SET_NULL,
                                null=True, blank=True)
    year_of_added = models.CharField(max_length=255, null=True, blank=True)
    faculty = models.CharField(max_length=255, choices=Faculty)
    registration_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    data = models.JSONField(null=True, blank=True)


class Course(models.Model):
    teacher = models.ForeignKey('teachers_admin.Teacher', on_delete=models.SET_NULL, blank=True, null=True)
    auditoire = models.ManyToManyField('main.Auditoire',related_name="course_auditoire")
    faculty = models.CharField(max_length=255, choices=Faculty)
    title = models.CharField(max_length=255)
    image = models.ImageField(default='/static/admin/assets/images/logo-mobile.png')
    notes = models.TextField(verbose_name='note', null=True, blank=True)
    pdf_files = models.FileField(upload_to='cours_pdfs/')
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
    def image_url(self):
        return (self.image and hasattr(self.image, 'url') and self.image.url) or '/static/assets/university_mobile_logo_ulc-1 (1).png'

class StudentCourses(models.Model):
    student = models.ForeignKey(Student, related_name="student_courses", on_delete=models.CASCADE)
    courses = models.ForeignKey(Course, on_delete=models.CASCADE)
    auditoire = models.ForeignKey('main.Auditoire', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class Alumni(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    diploma = models.CharField(max_length=255)
    diploma_year = models.IntegerField()
    is_deleted = models.BooleanField(default=False)


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


class NewsletterEmail(models.Model):
    email = models.EmailField(unique=True)

# Create your models here.
