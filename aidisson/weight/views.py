from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .forms import WeightCreateForm
from .models import Log



class WeightListView(ListView):
    queryset = Log.objects.all()
    


class WeightCreateView(CreateView):
    form_class = WeightCreateForm
    template_name = 'weight/form.html'
    success_url = "/weight/"
