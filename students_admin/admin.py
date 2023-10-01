from django.contrib import admin

from students_admin.models import *

admin.site.register(Student)
admin.site.register(StudentCourses)

# Register your models here.
