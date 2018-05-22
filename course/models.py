from django.db import models
from django.db.models import CASCADE

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
    course = models.ForeignKey(Course, on_delete=CASCADE)
    period = models.ForeignKey(Period, on_delete=CASCADE)
    students = models.ManyToManyField(StudentProfile)

    def __str__(self):
        return "{0}, {1}".format(self.name, self.course.name)


class Term(models.Model):
    name = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()


# Things that Students and Teachers probably care about


class GradingCategory(models.Model):
    course = models.ForeignKey(Course, on_delete=CASCADE)
    name = models.TextField(max_length=50)
    weight = models.IntegerField()

    def __str__(self):
        return "{0}: {1} - {2}".format(self.course.name, self.name, self.weight)


class Announcement(models.Model):
    course = models.ForeignKey(Course, on_delete=CASCADE)
    pinned = models.BooleanField(default=False)
    announcement = models.TextField(max_length=140)
    shown = models.BooleanField(default=True)

    def __str__(self):
        return self.announcement[1:20]


class Assignment(models.Model):
    term = models.ForeignKey(Term, null=True, on_delete=CASCADE)
    category = models.ForeignKey(GradingCategory, null=True, on_delete=CASCADE)
    name = models.TextField()
    description = models.TextField()
    out_of = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=CASCADE)
    due_by = models.DateField()

    def __str__(self):
        return self.name


class AssignmentSubmission(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=CASCADE)
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
    course = models.ForeignKey(Course, on_delete=CASCADE)

    def __str__(self):
        return "{0} - {1}".format(self.letter, self.percent)


class CourseGrade(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=CASCADE)
    term = models.ForeignKey(Term, on_delete=CASCADE)
    course = models.ForeignKey(Course, related_name='course_grade', on_delete=CASCADE)
    percent = models.IntegerField()

    def __str__(self):
        return "{0}: {1} {2} - {3}%".format(self.course.name, self.student.user.first_name, self.student.user.last_name,
                                            self.percent)
