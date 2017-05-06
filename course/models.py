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
    name = models.TextField(max_length=50)
    weight = models.IntegerField()

    def __str__(self):
        return "{0}: {1} - {2}".format(self.course.name, self.name, self.weight)


class Announcement(models.Model):
    course = models.ForeignKey(Course)
    pinned = models.BooleanField(default=False)
    announcement = models.TextField(max_length=140)

    def __str__(self):
        return self.announcement[1:20]


class Assignment(models.Model):
    category = models.ForeignKey(GradingCategory, null=True)
    name = models.TextField()
    description = models.TextField()
    out_of = models.IntegerField()
    course = models.ForeignKey(Course)
    due_by = models.DateField()

    def __str__(self):
        return self.name


class AssignmentSubmission(models.Model):
    student = models.ForeignKey(StudentProfile)
    assignment = models.ForeignKey(Assignment)
    grade = models.IntegerField()
    comments = models.TextField()
    submission_type = models.CharField(choices=SUBMISSION_TYPES, max_length=4)
    body = models.TextField(null=True)
    graded = models.BooleanField(default=False)

    def __str__(self):
        return self.student.user.first_name


# Mostly Teacher stuff


class LetterGrade(models.Model):
    letter = models.CharField(choices=LETTER_GRADES, max_length=2)
    percent = models.IntegerField()
    course = models.ForeignKey(Course)

    def __str__(self):
        return "{0} - {1}".format(self.letter, self.percent)


class CourseGrade(models.Model):
    student = models.ForeignKey(StudentProfile)
    course = models.ForeignKey(Course, related_name='course_grade')
    percent = models.IntegerField()

    def __str__(self):
        return "{0}: {1} {2} - {3}%".format(self.course.name, self.student.user.first_name, self.student.user.last_name, self.percent)
