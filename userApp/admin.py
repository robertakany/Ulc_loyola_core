from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from userApp.models import  User

from students_admin.models import Student
from teachers_admin.models import Teacher



# Register your models here.


class StudentInline(admin.TabularInline):
    model = Student

class TeacherInline(admin.TabularInline):
    model = Teacher


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email', 'username', 'first_name',)
    list_filter = ('email', 'username', 'first_name', 'is_active', 'is_staff')
    readonly_fields = ('date_joined',)
    list_display = ( 'email', 'avatar_tag', 'username', 'first_name',
                    'is_teacher', 'is_student')

    fieldsets = (
        ('Identity', {'fields': ('first_name', 'last_name', 'country', 'address', 'role', 'born_date', 'sexe_type')}),
        ('Photo profile', {'fields': ('avatar',)}),
        ('Security', {'fields': ('username', 'phone', 'email', 'password')}),
        ('Access', {'fields': ('is_active', 'is_superuser', 'is_staff',
         'is_teacher', 'is_student', 'is_delete', 'user_permissions')}),
        ('More', {'fields': ('slug', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'email', 'phone', 'password1', 'password2', 'avatar', 'is_active', 'is_staff')}
         ),
    )

    inlines = [
        StudentInline,
        TeacherInline
    ]


admin.site.register(User, UserAdminConfig)