from rest_framework import viewsets
from rest_framework.decorators import detail_route
from course.serializers import CourseSerializer, PeriodSerializer, AssignmentSerializer, AssignmentSubmissionSerializer, \
    HourSerializer, AssignmentCreateSerializer
from course.models import Course, Period, Assignment, AssignmentSubmission, Hour
from users.models import TeacherProfile, StudentProfile
from django.db.models import Q
from course.filters import CourseFilterBackend, HourFilterBackend, AssignmentFilterBackend, AssignmentSubmissionFilterBackend
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


class AssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()
    filter_backends = [
        AssignmentFilterBackend
    ]


    def get_serializer_class(self):
        if self.request.method == "POST":
            return AssignmentCreateSerializer
        else:
            return AssignmentSerializer


class AssignmentSubmissionViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentSubmissionSerializer
    queryset = AssignmentSubmission.objects.all()
    filter_backends = [
        AssignmentSubmissionFilterBackend
    ]
