from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import User
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

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

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('index')

class CustomRegistrationView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'users/profile.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return self.request.user