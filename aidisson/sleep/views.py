from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .forms import SessionCreateForm
from .models import Session



class SleepListView(ListView):
    queryset = Session.objects.all()



class SleepCreateView(CreateView):
    form_class = SessionCreateForm
    template_name = 'sleep/form.html'
    success_url = "/sleep/"
