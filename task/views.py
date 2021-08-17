from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, CreateView

from .forms import ContactResponseForm


class HomeView(TemplateView):
    template_name = 'task/done.html'


class SubmitFormView(CreateView):
    template_name = 'task/index.html'
    form_class = ContactResponseForm
    success_url = "/submitted/"
