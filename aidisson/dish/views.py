from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .forms import MealCreateForm
from .models import Meal



class MealListView(ListView):
    queryset = Meal.objects.all()
    


class MealCreateView(CreateView):
    form_class = MealCreateForm
    template_name = 'dish/form.html'
    success_url = "/diet/"
