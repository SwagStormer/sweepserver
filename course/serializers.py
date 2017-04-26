from rest_framework import serializers
from course.models import Course, Period, Assignment, AssignmentSubmission, Hour
from users.models import StudentProfile
from users.serializers import StudentProfileSerializer,  TeacherProfileSerializer


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class CourseNameSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Course
        exclude = ('teachers', 'students')


class HourSerializer(serializers.ModelSerializer):
    students = StudentProfileSerializer(many=True, read_only=True)

    class Meta:
        model = Hour
        fields = '__all__'

    def create(self, validated_data):
        hour = Hour(**validated_data)
        hour.save()
        return hour


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = '__all__'


class AssignmentSerializer(serializers.ModelSerializer):
    course = CourseNameSerializer(read_only=True, allow_null=True)

    class Meta:
        model = Assignment
        fields = '__all__'


class AssignmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'


class AssignmentSubmissionSerializer(serializers.ModelSerializer):
    assignment = AssignmentSerializer(read_only=True)
    student = StudentProfileSerializer(read_only=True)

    class Meta:
        model = AssignmentSubmission
        fields = '__all__'
