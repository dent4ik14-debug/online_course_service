from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from courses.models import Course
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'role']
    def save(self, commit=True):
        user = super().save(commit=commit)

        if commit:
            if user.role == 'teacher':
                content_type = ContentType.objects.get_for_model(Course)
                add_course_perm = Permission.objects.get(
                    codename='add_course', content_type=content_type
                )
                user.user_permissions.add(add_course_perm)
        return user