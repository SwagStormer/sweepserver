from django.contrib import admin

# Register your models here.

from django.contrib import admin

from course.models import Course, Period, Assignment, AssignmentSubmission, Hour


class CourseAdmin(admin.ModelAdmin):
    pass
admin.site.register(Course, CourseAdmin)


class PeriodAdmin(admin.ModelAdmin):
    pass
admin.site.register(Period, PeriodAdmin)


class HourAdmin(admin.ModelAdmin):
    pass
admin.site.register(Hour, HourAdmin)


class AssignmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Assignment, AssignmentAdmin)


class AssignmentSubmissionAdmin(admin.ModelAdmin):
    pass
admin.site.register(AssignmentSubmission, AssignmentSubmissionAdmin)