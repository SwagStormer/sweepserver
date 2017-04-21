from rest_framework import viewsets
from course.serializers import CourseSerializer, PeriodSerializer, AssignmentSerializer, AssignmentSubmissionSerializer
from course.models import Course, Period, Assignment, AssignmentSubmission
# Create your views here.


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class PeriodViewSet(viewsets.ModelViewSet):
    serializer_class = PeriodSerializer
    queryset = Period.objects.all()


class AssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()


class AssignmentSubmissionViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentSubmission
    queryset = AssignmentSubmission.objects.all()