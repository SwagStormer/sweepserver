from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class BaseUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=True)


class StudentProfile(models.Model):
    user = models.ForeignKey(BaseUser)

    def __str__(self):
        return self.user.first_name


class TeacherProfile(models.Model):
    user = models.ForeignKey(BaseUser)
    courses = models.ManyToManyField('course.Course', related_query_name='teachers', blank=True)

    def __str__(self):
        return self.user.username
