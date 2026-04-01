from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Roles', {'fields': ('is_student', 'is_teacher', 'is_admin')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Roles', {'fields': ('is_student', 'is_teacher', 'is_admin')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name',
                    'is_student', 'is_teacher', 'is_admin', 'is_staff')
