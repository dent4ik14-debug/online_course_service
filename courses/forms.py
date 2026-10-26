from django import forms
from .models import Course


# 1. Віджет, який офіційно дозволяє мультизавантаження
class MultipleFileInput(forms.ClearableFileInput):
  allow_multiple_selected = True


# 2. Поле, що правильно валідує список файлів
class MultipleFileField(forms.FileField):

  def __init__(self, *args, **kwargs):
    kwargs.setdefault('widget', MultipleFileInput())
    super().__init__(*args, **kwargs)

  def clean(self, data, initial=None):
    single_file_clean = super().clean
    if isinstance(data, (list, tuple)):
      result = [single_file_clean(d, initial) for d in data]
    else:
      result = single_file_clean(data, initial)
    return result


class CourseForm(forms.ModelForm):
  files = MultipleFileField(required=False, label='Файли курсу')

  class Meta:
    model = Course
    fields = ['name', 'description', 'category']