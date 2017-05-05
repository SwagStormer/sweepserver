from rest_framework import viewsets
from course.serializers import CourseSerializer, PeriodSerializer, AssignmentSerializer, AssignmentSubmissionSerializer, \
    HourSerializer, AssignmentCreateSerializer, CourseGradeSerializer, \
    LetterGradeSerializer, GradingCategorySerializer, AnnouncementSerializer
from course.models import Course, Period, Assignment, AssignmentSubmission, Hour, \
    CourseGrade, LetterGrade, GradingCategory, Announcement
from course.filters import CourseFilterBackend, HourFilterBackend, AssignmentFilterBackend, \
    AssignmentSubmissionFilterBackend
# Create your views here.


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    filter_backends = [
        CourseFilterBackend
    ]


class PeriodViewSet(viewsets.ModelViewSet):
    serializer_class = PeriodSerializer
    queryset = Period.objects.all()


class HourViewSet(viewsets.ModelViewSet):
    serializer_class = HourSerializer
    queryset = Hour.objects.none()
    filter_backends = [
        HourFilterBackend
    ]


class AnnouncementViewSet(viewsets.ModelViewSet):
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all()


class AssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()
    filter_backends = [
        AssignmentFilterBackend
    ]


class AssignmentSubmissionViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentSubmissionSerializer
    queryset = AssignmentSubmission.objects.all()
    filter_backends = [
        AssignmentSubmissionFilterBackend
    ]


class CourseGradeViewSet(viewsets.ModelViewSet):
    serializer_class = CourseGradeSerializer
    queryset = CourseGrade.objects.all()


class LetterGradeViewSet(viewsets.ModelViewSet):
    serializer_class = LetterGradeSerializer
    queryset = LetterGrade.objects.all()


class GradingCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = GradingCategorySerializer
    queryset = GradingCategory.objects.all()


