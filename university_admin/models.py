from django.db import models


from students_admin.models import Student


class Registration(models.Model):
    student = models.ForeignKey(Student, related_name="student_register", on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    data = models.JSONField(null=True, blank=True)


class PdfCourse(models.Model):
    teacher = models.ForeignKey('teachers_admin.Teacher', on_delete=models.CASCADE)
    audience = models.ForeignKey('main.Audience', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    warning = models.TextField(null=True, blank=True)
    pdf_files = models.FileField(upload_to='cours_pdfs/')
    date_of_register = models.DateTimeField(auto_now_add=True)
    data = models.JSONField(null=True, blank=True)


class StudentCourses(models.Model):
    student = models.ForeignKey(Student, related_name="student_courses", on_delete=models.CASCADE)
    courses = models.ForeignKey(PdfCourse, on_delete=models.CASCADE)
    audience = models.ForeignKey('main.Audience', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class TeacherStudentRelation(models.Model):
    Teacher = models.ForeignKey('teachers_admin.Teacher', related_name="teachers", null=True, blank=True, on_delete=models.CASCADE)
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
