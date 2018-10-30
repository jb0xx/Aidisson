from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .forms import WorkoutCreateForm
from .models import Workout


class WorkoutListView(ListView):
    queryset = Workout.objects.all()


class WorkoutCreateView(CreateView):
    form_class = WorkoutCreateForm
    template_name = 'exercise/form.html'
    success_url = "/exercise/"