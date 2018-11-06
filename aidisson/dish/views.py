from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .forms import MealCreateForm
from .models import Meal



class MealCreateView(LoginRequiredMixin, CreateView):
    form_class = MealCreateForm
    template_name = 'dish/meal_list.html'
    success_url = '/diet/'
    # login_url = '/login/' 	# can be defaulted in settings.py

    def form_valid(self, form):
    	instance = form.save(commit=False)
    	instance.trainee = self.request.user.trainee
    	return super(MealCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        trainee = self.request.user.trainee
        object_list = Meal.objects.filter(trainee=trainee)
        kwargs['object_list'] = object_list.order_by('-datetime')
        return super(MealCreateView, self).get_context_data(**kwargs)