from django.shortcuts import render
from django.views.generic import ListView
from .models import Course, CourseCategory
# Create your views here.
class CoursesList(ListView):
    model = Course
    template_name = 'courses/course_list.html'
    title = 'Список Курсів'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = CourseCategory.objects.all()

        category_id = self.request.GET.get('category_id')
        if category_id and category_id.isdigit():
            context['curent_category'] = CourseCategory.objects.filter(id=category_id).first()
        return context