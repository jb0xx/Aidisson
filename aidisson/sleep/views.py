from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .forms import SessionCreateForm
from .models import Session



# class SleepListView(ListView):
#     queryset = Session.objects.all()



class SleepCreateView(LoginRequiredMixin, CreateView):
    form_class = SessionCreateForm
    template_name = 'sleep/session_list.html'
    success_url = '/sleep/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.trainee = self.request.user.trainee
        return super(SleepCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        trainee = self.request.user.trainee
        object_list = Session.objects.filter(trainee=trainee)
        kwargs['object_list'] = object_list.order_by('starttime')
        return super(SleepCreateView, self).get_context_data(**kwargs)