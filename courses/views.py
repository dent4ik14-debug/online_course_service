from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import ListView, DetailView
from .models import Course, CourseCategory, Video
from users.models import User
from .forms import CourseForm
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

@login_required
@permission_required(
    'courses.add_course', raise_exception=True
)
def add_course(request):
  if request.method == 'POST':
    form = CourseForm(request.POST, request.FILES)
    files = request.FILES.getlist('files')

    if form.is_valid():
      course = form.save(commit=False)
      course.authot = request.user
      course.save()
      for f in files:
        Video.objects.create(
            course=course,
            video_file=f,
            title=f.name,
        )
      return redirect('courses:course_detail', pk=course.pk)
  else:
    form = CourseForm()

  return render(request, 'courses/add_course.html', {'form': form})