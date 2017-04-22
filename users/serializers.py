from rest_framework import serializers
from users.models import BaseUser, StudentProfile, TeacherProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = '__all__'

    def create(self, validated_data):
        user = BaseUser(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        user.set_password(validated_data["password"])
        user.save()
        print(user)
        if user.is_teacher:
            TeacherProfile(user=user).save()
        else:
            StudentProfile(user=user).save()
        return user


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
