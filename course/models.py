from django.db import models
from users.models import TeacherProfile, StudentProfile

# Create your models here.


SUBMISSION_TYPES = (
    ('FILE', 'file'),
    ('TEXT', 'text'),
)


LETTER_GRADES = (
    ('A', 'A'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B', 'B'),
    ('B-', 'B-'),
    ('C+', "C+"),
    ('C', "C"),
    ('C-', "C-"),
    ('D+', 'D+'),
    ('D', 'D'),
    ('D-', 'D-'),

)


class Course(models.Model):
    name = models.TextField()
    students = models.ManyToManyField(StudentProfile, blank=True)

    def __str__(self):
        return self.name


# Scheduling stuff

class Period(models.Model):
    name = models.TextField()
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name


class Hour(models.Model):
    name = models.TextField()
    course = models.ForeignKey(Course)
    period = models.ForeignKey(Period)
    students = models.ManyToManyField(StudentProfile)

    def __str__(self):
        return "{0}, {1}".format(self.name, self.course.name)


# Things that Students and Teachers probably care about


class GradingCategory(models.Model):
    course = models.ForeignKey(Course)
    weight = models.IntegerField()


class Announcement(models.Model):
    course = models.ForeignKey(Course)
    pinned = models.BooleanField(default=False)
    announcement = models.TextField(max_length=140)


class Assignment(models.Model):
    category = models.ForeignKey(GradingCategory, null=True)
    name = models.TextField()
    description = models.TextField()
    out_of = models.IntegerField()
    course = models.ForeignKey(Course)
    due_by = models.DateField()


class AssignmentSubmission(models.Model):
    student = models.ForeignKey(StudentProfile)
    assignment = models.ForeignKey(Assignment)
    grade = models.IntegerField()
    comments = models.TextField()
    submission_type = models.CharField(choices=SUBMISSION_TYPES, max_length=4)
    body = models.TextField(null=True)
    graded = models.BooleanField(default=False)


# Mostly Teacher stuff

class GradingScale(models.Model):
    course = models.ForeignKey(Course)


class LetterGrade(models.Model):
    letter = models.CharField(choices=LETTER_GRADES, max_length=2)
    percent = models.IntegerField()
    course = models.ForeignKey(GradingScale)


class CourseGrade(models.Model):
    student = models.ForeignKey(StudentProfile)
    course = models.ForeignKey(Course)
    percent = models.IntegerField()
