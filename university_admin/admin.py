from django.contrib import admin
from university_admin.models import *


admin.site.register(Course)
admin.site.register(StudentCourses)
admin.site.register(TeacherStudentRelation)
admin.site.register(Alumni)


# Register your models here.
