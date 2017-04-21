from rest_framework import serializers
from course.models import Course, Period, Assignment, AssignmentSubmission
from users.serializers import StudentProfileSerializer,  TeacherProfileSerializer


class CourseSerializer(serializers.ModelSerializer):
    teachers = TeacherProfileSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = '__all__'


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'


class AssignmentSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentSubmission
        fields = '__all__'
