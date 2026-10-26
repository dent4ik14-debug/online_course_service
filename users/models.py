from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email = models.EmailField('email address', unique=True)

    class Role(models.TextChoices):
        TEACHER = 'teacher', 'Викладач'
        STUDENT = 'student', 'Студент'
        
    role = models.CharField(
        'роль',
        max_length=10,
        choices=Role.choices,
        default=Role.STUDENT,
    )