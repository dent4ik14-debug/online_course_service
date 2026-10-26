from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import User

class UsersList(ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'teachers'

    def get_queryset(self):
        return User.objects.filter(role=User.Role.TEACHER)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список Викладачів'
        return context

class AboutAuthor(DetailView):
    model = User
    template_name = 'users/about_author.html'
    context_object_name = 'author'

    def get_queryset(self):
            return super().get_queryset().prefetch_related('courses_created')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Про Викладача'
        return context