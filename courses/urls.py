from django.contrib import admin
from django.urls import path
from .views import CoursesList

app_name = 'courses'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CoursesList.as_view(), name='courses_list')
]