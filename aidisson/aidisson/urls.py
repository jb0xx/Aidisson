"""aidisson URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

from weight.views import WeightListView, WeightCreateView
from sleep.views import SleepListView, SleepCreateView
from exercise.views import WorkoutListView, WorkoutCreateView
from dish.views import MealListView, MealCreateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^about/$', TemplateView.as_view(template_name='about.html')),
    url(r'^weight/$', WeightListView.as_view()),
    url(r'^weight/create/$', WeightCreateView.as_view()),
    url(r'^sleep/$', SleepListView.as_view()),
    url(r'^sleep/create/$', SleepCreateView.as_view()),
    url(r'^exercise/$', WorkoutListView.as_view()),
    url(r'^exercise/create/$', WorkoutCreateView.as_view()),
    url(r'^diet/$', MealListView.as_view()),
    url(r'^diet/create/$', MealCreateView.as_view()),
    
    # url(r'^restaurants/(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view()),
    
]



