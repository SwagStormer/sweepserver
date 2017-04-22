from django.db import models
from users.models import TeacherProfile, StudentProfile

# Create your models here.


SUBMISSION_TYPES = (
    ('FILE', 'file'),
    ('TEXT', 'text'),
)


class Course(models.Model):
    name = models.TextField()
    teachers = models.ManyToManyField(TeacherProfile, blank=True)
    students = models.ManyToManyField(StudentProfile, blank=True)


class Period(models.Model):
    name = models.TextField()
    courses = models.ManyToManyField(Course)


class Hour(models.Model):
    name = models.TextField()
    course = models.ForeignKey(Course)
    period = models.ForeignKey(Period)
    students = models.ManyToManyField(StudentProfile)


class Assignment(models.Model):
    name = models.TextField()
    description = models.TextField()
    out_of = models.IntegerField()
    course = models.ForeignKey(Course)


class AssignmentSubmission(models.Model):
    student = models.ForeignKey(StudentProfile)
    assignment = models.ForeignKey(Assignment)
    submission_type = models.CharField(choices=SUBMISSION_TYPES, max_length=4)
    body = models.TextField(null=True)

