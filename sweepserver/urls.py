"""sweepserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from users.views import UserViewSet, TeacherProfileViewSet, StudentProfileViewSet, token_auth_thing
from course.views import CourseViewSet, PeriodViewSet, AssignmentViewSet, AssignmentSubmissionViewSet, HourViewSet, \
    CourseGradeViewSet, LetterGradeViewSet, GradingCategoryViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teachers', TeacherProfileViewSet)
router.register(r'students', StudentProfileViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'periods', PeriodViewSet)
router.register(r'hours', HourViewSet)
router.register(r'assignments', AssignmentViewSet)
router.register(r'assignment_submissions', AssignmentSubmissionViewSet)
router.register(r'grade_categories', GradingCategoryViewSet)
router.register(r'course_grades', CourseGradeViewSet)
router.register(r'letter_grades', LetterGradeViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'api-token-auth/', token_auth_thing),
    url(r'api/', include(router.urls))
]
