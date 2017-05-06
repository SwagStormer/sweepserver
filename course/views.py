from rest_framework import viewsets
from rest_framework.decorators import detail_route
from django.http import JsonResponse
from course.serializers import CourseSerializer, PeriodSerializer, AssignmentSerializer, AssignmentSubmissionSerializer, \
    HourSerializer, AssignmentCreateSerializer, CourseGradeSerializer, \
    LetterGradeSerializer, GradingCategorySerializer, AnnouncementSerializer, CourseWithGradeSerializer
from course.models import Course, Period, Assignment, AssignmentSubmission, Hour, \
    CourseGrade, LetterGrade, GradingCategory, Announcement
from users.models import StudentProfile
from course.filters import CourseFilterBackend, HourFilterBackend, AssignmentFilterBackend, \
    AssignmentSubmissionFilterBackend
# Create your views here.


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    filter_backends = [
        CourseFilterBackend
    ]

    @detail_route(methods=["GET"])
    def grade(self, request, pk=None):
        # Get all assignments
        submissions = AssignmentSubmission.objects.filter(student__user=request.user, assignment__course=pk)

        final_grade = 0

        for submission in submissions:
            percent = submission.grade / submission.assignment.out_of
            if submission.assignment.category is not None:
                print(submission.assignment.category)
                percent *= submission.assignment.category.weight
            final_grade += percent
        final_grade *= 100
        try:
            course_grade = CourseGrade.objects.get(student__user=request.user, course__id=pk)
            course_grade.percent = final_grade
            course_grade.save()
        except Exception:
            c = CourseGrade(
                student=StudentProfile.objects.get(user=request.user),
                course=Course.objects.get(id=pk),
                percent=final_grade
            )
            c.save()
        return JsonResponse({"course": pk, "grade": final_grade})


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


