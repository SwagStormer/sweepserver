from rest_framework import serializers
from course.models import Course, Period, Assignment, AssignmentSubmission, \
    Hour, CourseGrade, LetterGrade, GradingCategory, Announcement, Term
from users.serializers import StudentProfileSerializer


class CourseGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseGrade
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class HourSerializer(serializers.ModelSerializer):

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


class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = '__all__'


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'


class AssignmentSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)

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


class LetterGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LetterGrade
        fields = '__all__'


class GradingCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GradingCategory
        fields = '__all__'
