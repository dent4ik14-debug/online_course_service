from django.db import models
from django.core.validators import FileExtensionValidator
from users.models import User
# Create your models here.
class CourseCategory(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
    

class Course(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    authot = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='courses_created',)
    category = models.ForeignKey(to=CourseCategory, on_delete=models.SET_NULL, null=True, blank=True)
    

class Video(models.Model):
    title = models.CharField(max_length=128)
    video_file = models.FileField(
        upload_to='videos/', 
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'webm', 'mkv'])]
    )
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title