from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

# fmt: off
urlpatterns = [
    path("register/",
         views.StudentRegistrationView.as_view(),
         name="student_registration",),
    path("enroll-course/",
         views.StudentEnrollCourseView.as_view(),
         name="student_enroll_course",),
    path("register/",
         views.StudentRegistrationView.as_view(),
         name="student_registration",),
    path("courses/",
         views.StudentsCourseListView.as_view(),
         name="student_course_list"),
    path("course/<pk>/",
         cache_page(60 * 15)(views.StudentsCourseDetailView.as_view()),
         name="student_course_detail",),
    path("course/<pk>/<module_id>/",
         cache_page(60 * 15)(views.StudentsCourseDetailView.as_view()),
         name="student_course_detail_module",),
]
# fmt: on
