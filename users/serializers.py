from rest_framework import serializers
from users.models import BaseUser, StudentProfile, TeacherProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = '__all__'


class UserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        exclude = ('password', )


class StudentProfileSerializer(serializers.ModelSerializer):
    user = UserReadSerializer(read_only=True)

    class Meta:
        model = StudentProfile
        fields = '__all__'


class TeacherProfileSerializer(serializers.ModelSerializer):
    user = UserReadSerializer(read_only=True)

    class Meta:
        model = TeacherProfile
        fields = '__all__'
