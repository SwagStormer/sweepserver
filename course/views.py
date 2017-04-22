from rest_framework import viewsets
from course.serializers import CourseSerializer, PeriodSerializer, AssignmentSerializer, AssignmentSubmissionSerializer, \
    HourSerializer
from course.models import Course, Period, Assignment, AssignmentSubmission, Hour
from users.models import TeacherProfile, StudentProfile
from django.db.models import Q


# Create your views here.


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_queryset(self):
        q = self.request.query_params.get
        user = self.request.user
        if user.is_authenticated:
            is_teacher = True if user.is_teacher else False
            if is_teacher:
                teacher = TeacherProfile.objects.filter(user=user)
                queryset = Course.objects.filter(teachers__in=teacher)
            else:
                student = StudentProfile.objects.filter(user=user)
                queryset = Course.objects.filter(students__in=student)
            return queryset

        else:
            pass


class PeriodViewSet(viewsets.ModelViewSet):
    serializer_class = PeriodSerializer
    queryset = Period.objects.all()


class HourViewSet(viewsets.ModelViewSet):
    serializer_class = HourSerializer
    queryset = Hour.objects.none()

    def get_queryset(self):
        q = self.request.query_params.get
        user = self.request.user
        if user.is_authenticated:
            is_teacher = True if user.is_teacher else False
            if is_teacher:
                teacher = TeacherProfile.objects.filter(user=user)
                courses = Course.objects.filter(teachers__in=teacher)
            else:
                student = StudentProfile.objects.filter(user=user)
                courses = Course.objects.filter(students__in=student)
            queryset = Hour.objects.filter(course=courses)

            if q('course'):
                queryset.filter(course=q('course'))
            if q('search'):
                queryset.filter(name__icontains=q('search'))
            return queryset
        else:
            pass



class AssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.none()

    def get_queryset(self):
        q = self.request.query_params.get
        user = self.request.user
        if user.is_authenticated:
            is_teacher = True if user.is_teacher else False
            if is_teacher:
                teacher = TeacherProfile.objects.filter(user=user)
                courses = Course.objects.filter(teachers__in=teacher)
            else:
                student = StudentProfile.objects.filter(user=user)
                courses = Course.objects.filter(students__in=student)
            queryset = Assignment.objects.filter(course=courses)

            if q('course'):
                queryset.filter(course=q('course'))
            if q('search'):
                queryset.filter(name__icontains=q('search'))
            return queryset
        else:
            pass


class AssignmentSubmissionViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentSubmissionSerializer
    queryset = AssignmentSubmission.objects.all()
