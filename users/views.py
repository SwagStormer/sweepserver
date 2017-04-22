from rest_framework import viewsets
from users.serializers import UserReadSerializer, UserSerializer, TeacherProfileSerializer, StudentProfileSerializer
from users.models import BaseUser, StudentProfile, TeacherProfile
from rest_framework.exceptions import AuthenticationFailed

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = BaseUser.objects.none()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return UserSerializer
        return UserReadSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.request.user
        else:
            raise AuthenticationFailed()


class TeacherProfileViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherProfileSerializer
    queryset = TeacherProfile.objects.all()


class StudentProfileViewSet(viewsets.ModelViewSet):
    serializer_class = StudentProfileSerializer
    queryset = StudentProfile.objects.all()

