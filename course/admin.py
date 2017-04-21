from django.contrib import admin

# Register your models here.

from django.contrib import admin

from course.models import Course, Period, Assignment, AssignmentSubmission


class CourseAdmin(admin.ModelAdmin):
    pass
admin.site.register(Course, CourseAdmin)


class PeriodAdmin(admin.ModelAdmin):
    pass
admin.site.register(Period, PeriodAdmin)


class AssignmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Assignment, AssignmentAdmin)


class AssignmentSubmissionAdmin(admin.ModelAdmin):
    pass
admin.site.register(AssignmentSubmission, AssignmentSubmissionAdmin)