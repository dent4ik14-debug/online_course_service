from django.views.generic.base import TemplateView

class Index(TemplateView):
    template_name = 'courses/index.html'
    title = 'Домашня сторінка'
