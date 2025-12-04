from django.urls import path
from django.views.generic import TemplateView

app_name = 'tasks'

urlpatterns = [
    path('', TemplateView.as_view(template_name='tasks/home.html', name='home'), name='home'),
    path('help/', TemplateView.as_view(template_name='tasks/help.html'), name='help'),
]