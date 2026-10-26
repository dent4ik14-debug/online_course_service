from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Course, CourseCategory
from users.models import User
# Create your views here.
class CoursesList(ListView):
    model = Course
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.GET.get('category_id')
        if category_id and category_id.isdigit():
            queryset = queryset.filter(category_id=category_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список Курсів'
        context['categories'] = CourseCategory.objects.all()
        category_id = self.request.GET.get('category_id')
        if category_id and category_id.isdigit():
            context['curent_category'] = CourseCategory.objects.filter(id=category_id).first()
        return context

class AboutCourse(DetailView):
    model = Course
    template_name = 'courses/about_course.html'
    context_object_name = 'course'

    def get_queryset(self):
        return super().get_queryset().prefetch_related('videos')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Про курс'
        return context