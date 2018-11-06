from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .forms import WorkoutCreateForm
from .models import Workout



class WorkoutCreateView(LoginRequiredMixin, CreateView):
    form_class = WorkoutCreateForm
    template_name = 'exercise/workout_list.html'
    success_url = '/exercise/'

    def form_valid(self, form):
    	instance = form.save(commit=False)
    	instance.trainee = self.request.user.trainee
    	return super(WorkoutCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        trainee = self.request.user.trainee
        object_list = Workout.objects.filter(trainee=trainee)
        kwargs['object_list'] = object_list.order_by('starttime')
        return super(WorkoutCreateView, self).get_context_data(**kwargs)
