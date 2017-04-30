from django.db.models import Q
from rest_framework.filters import BaseFilterBackend
from users.models import TeacherProfile, StudentProfile
from course.models import Course, Hour, Assignment, AssignmentSubmission


class CourseFilterBackend(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        q = request.query_params.get
        user = request.user
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


class HourFilterBackend(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        q = request.query_params.get
        user = request.user
        if user.is_authenticated:
            is_teacher = True if user.is_teacher else False
            if is_teacher:
                teacher = TeacherProfile.objects.filter(user=user)
                courses = Course.objects.filter(teachers=teacher)
            else:
                student = StudentProfile.objects.filter(user=user)
                courses = Course.objects.filter(students__in=student)
            queryset = Hour.objects.filter(course__in=courses)
            if q('course'):
                queryset = queryset.filter(course=q('course'))
            if q('search'):
                queryset = queryset.filter(name__icontains=q('search'))
            return queryset
        else:
            pass


class AssignmentFilterBackend(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        queryset = Assignment.objects.all()
        q = request.query_params.get
        user = request.user
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
            queryset = queryset.order_by('due_by')
        return queryset


class AssignmentSubmissionFilterBackend(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        q = request.query_params.get
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
            queryset = queryset.filter(
                Q(assignment__name__icontains=q('search')) | Q(student__user__first_name__icontains=q('search')))
        if q('assignment'):
            queryset = queryset.filter(assignment=q('assignment'))
        return queryset


