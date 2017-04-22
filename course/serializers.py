from rest_framework import serializers
from course.models import Course, Period, Assignment, AssignmentSubmission, Hour
from users.serializers import StudentProfileSerializer,  TeacherProfileSerializer


class CourseSerializer(serializers.ModelSerializer):
    teachers = TeacherProfileSerializer(many=True, read_only=True)
    students = StudentProfileSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'


class HourSerializer(serializers.ModelSerializer):
    students = StudentProfileSerializer(many=True, read_only=True)

    class Meta:
        model = Hour
        fields = '__all__'

    def create(self, validated_data):
        hour = Hour(**validated_data)
        for student in hour.students:
            Course.objects.filter(hour.course).first().students.add(student)
        return hour


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
