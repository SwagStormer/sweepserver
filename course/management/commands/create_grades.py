from django.core.management.base import BaseCommand
from users.models import StudentProfile
from course.models import AssignmentSubmission, Course, CourseGrade


class Command(BaseCommand):
    help = "Update the list of needed items on the todo list"

    def handle(self, *args, **options):

        students = StudentProfile.objects.all()

        for student in students:

            courses = Course.objects.filter(students=student)

            for course in courses:

                submissions = AssignmentSubmission.objects.filter(student=student, assignment__course=course)
                final_grade = 0

                for submission in submissions:
                    percent = submission.grade / submission.assignment.out_of
                    if submission.assignment.category is not None:
                        percent *= submission.assignment.category.weight
                    final_grade += percent
                    print(final_grade)
                final_grade *= 100
                try:
                    course_grade = CourseGrade.objects.get(student=student, course=course)

                    course_grade.percent = final_grade
                    course_grade.save()
                except Exception:
                    c = CourseGrade(
                        student=student,
                        course=course,
                        percent=final_grade
                    )
                    c.save()
