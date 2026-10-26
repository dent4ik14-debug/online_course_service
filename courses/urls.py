from django.contrib import admin
from django.urls import path
from .views import CoursesList, AboutCourse

app_name = 'courses'

urlpatterns = [
    path('', CoursesList.as_view(), name='courses_list'),
    path('course/<int:pk>/', AboutCourse.as_view(), name='course_detail'),
]