from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .forms import WeightCreateForm
from .models import Log


class WeightListView(ListView):
    queryset = Log.objects.all()
    

class WeightCreateView(LoginRequiredMixin, CreateView):
    form_class = WeightCreateForm
    template_name = 'weight/log_list.html'
    success_url = '/weight/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.trainee = self.request.user.trainee
        return super(WeightCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        trainee = self.request.user.trainee
        object_list = Log.objects.filter(trainee=trainee)
        kwargs['object_list'] = object_list.order_by('log_datetime')
        return super(WeightCreateView, self).get_context_data(**kwargs)