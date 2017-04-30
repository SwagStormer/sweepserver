from rest_framework import viewsets
from users.serializers import UserReadSerializer, UserSerializer, TeacherProfileSerializer, StudentProfileSerializer
from users.models import BaseUser, StudentProfile, TeacherProfile
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
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

    def get_queryset(self):
        queryset = StudentProfile.objects.all()
        q = self.request.query_params.get
        if q('search'):
            queryset = queryset.filter(user__first_name__icontains=q('search'))
        if q('hour'):
            queryset = queryset.filter(hour=q('hour'))
        queryset = queryset.order_by('user__first_name')
        return queryset


class TokenAuthThing(ObtainAuthToken):
    def post(self, request, **kwargs):
        serializer = AuthTokenSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=401)

        token, created = Token.objects.get_or_create(user=serializer.validated_data['user'])
        username = serializer.validated_data['username']
        user_obj = BaseUser.objects.get(username=username)

        user_type = ''
        if user_obj.is_teacher:
            user_type = 'teacher'
        elif user_obj.is_student:
            user_type = 'student'

        return Response({'token': token.key, 'id': user_obj.id, 'type': user_type})

token_auth_thing = TokenAuthThing.as_view()
