from django.db import models
from users.models import TeacherProfile, StudentProfile

# Create your models here.


SUBMISSION_TYPES = (
    ('FILE', 'file'),
    ('TEXT', 'text'),
)


class Course(models.Model):
    name = models.TextField()
    teachers = models.ManyToManyField(TeacherProfile)
    students = models.ManyToManyField(StudentProfile)


class Period(models.Model):
    course = models.ForeignKey(Course)
    teacher = models.ManyToManyField(TeacherProfile)


class Assignment(models.Model):
    description = models.TextField()
    out_of = models.IntegerField()
    course = models.ForeignKey(Course)


class AssignmentSubmission(models.Model):
    student = models.ForeignKey(StudentProfile)
    assignment = models.ForeignKey(Assignment)
    submission = models.CharField(choices=SUBMISSION_TYPES, max_length=4)

