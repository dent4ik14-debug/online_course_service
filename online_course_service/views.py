from django.views.generic.base import TemplateView

class Index(TemplateView):
    template_name = 'courses/index.html'
    
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = 'Домашня сторінка'
            return context