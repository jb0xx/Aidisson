from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView

from dish.models import Meal
from exercise.models import Workout
from sleep.models import Session
from weight.models import Log


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        trainee = self.request.user.trainee
        context = super().get_context_data(**kwargs)
        context['weight'] = Log.objects.filter(trainee=trainee).order_by('-log_datetime')[0]
        context['meals'] = Meal.objects.filter(trainee=trainee).order_by('-datetime')[:3]
        context['workouts'] = Workout.objects.filter(trainee=trainee).order_by('-starttime')[:3]
        context['sleep_sessions'] = Session.objects.filter(trainee=trainee).order_by('-starttime')[:3]
        return context


# def get_context_data(self, *args, **kwargs):
#     context = super(IndexView, self).get_context_data(*args, **kwargs)
#     context['alphabetical_poll_list'] = Poll.objects.order_by('name')[:5]
#     return context 
