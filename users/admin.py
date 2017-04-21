from django.contrib import admin
from users.models import BaseUser, StudentProfile, TeacherProfile
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(BaseUser, UserAdmin)


class StudentProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(StudentProfile, StudentProfileAdmin)


class TeacherProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(TeacherProfile, TeacherProfileAdmin)