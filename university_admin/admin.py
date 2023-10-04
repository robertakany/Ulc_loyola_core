from django.contrib import admin
from university_admin.models import *

admin.site.register(Registration)
admin.site.register(Course)
admin.site.register(StudentCourses)
admin.site.register(TeacherStudentRelation)
admin.site.register(CalendrierAcademique)


# Register your models here.
