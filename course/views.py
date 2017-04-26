from rest_framework import viewsets
from rest_framework.decorators import detail_route
from course.serializers import CourseSerializer, PeriodSerializer, AssignmentSerializer, AssignmentSubmissionSerializer, \
    HourSerializer, AssignmentCreateSerializer
from course.models import Course, Period, Assignment, AssignmentSubmission, Hour
from users.models import TeacherProfile, StudentProfile
from django.db.models import Q


# Create your views here.


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_queryset(self):
        queryset = Course.objects.all()
        q = self.request.query_params.get
        user = self.request.user
        if user.is_authenticated:
            is_teacher = True if user.is_teacher else False
            if is_teacher:
                teacher = TeacherProfile.objects.get(user=user)
                Course.objects.filter(teachers=teacher)
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
    queryset = Assignment.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return AssignmentCreateSerializer
        else:
            return AssignmentSerializer


    def get_queryset(self):
        queryset = Assignment.objects.all()
        q = self.request.query_params.get
        user = self.request.user
        if user.is_authenticated:
            is_teacher = True if user.is_teacher else False
            if is_teacher:
                teacher = TeacherProfile.objects.get(user=user)
                courses = Course.objects.filter(teachers=teacher)
            else:
                student = StudentProfile.objects.get(user=user)
                courses = Course.objects.filter(students=student)
            queryset.filter(course=courses)
            if q('course'):
                queryset = queryset.filter(course=q('course'))
            if q('search'):
                queryset = queryset.filter(Q(name__icontains=q('search')) | Q(course__name__icontains=q('search')))
        return queryset


class AssignmentSubmissionViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentSubmissionSerializer
    queryset = AssignmentSubmission.objects.all()

    def get_queryset(self):
        q = self.request.query_params.get
        queryset = AssignmentSubmission.objects.all()
        if q('graded'):
            graded = True if q('graded') == 'true' else False
            print(graded)
            queryset = queryset.filter(graded=graded)
        if q('course'):
            queryset = queryset.filter(assignment__course=q('course'))
        if q('student'):
            queryset = queryset.filter(student=q('student'))
        if q('search'):
            queryset = queryset.filter(Q(assignment__name__icontains=q('search')) | Q(student__user__first_name__icontains=q('search')))
        if q('assignment'):
            queryset = queryset.filter(assignment=q('assignment'))
        return queryset
