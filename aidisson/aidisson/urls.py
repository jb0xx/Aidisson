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
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView

from dish.views import MealCreateView
from exercise.views import WorkoutCreateView
from sleep.views import SleepCreateView
from users.views import HomeView
from weight.views import WeightCreateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(template_name='home.html'), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^login/$', LoginView.as_view(), name='login'),

    url(r'^diet/$', MealCreateView.as_view(), name='diet'),
    url(r'^exercise/$', WorkoutCreateView.as_view(), name='exercise'),
    url(r'^sleep/$', SleepCreateView.as_view(), name='sleep'),
    # url(r'^weight/$', WeightListView.as_view(), name='weight'),
    url(r'^weight/$', WeightCreateView.as_view(), name='weight'),
    
    
    # url(r'^restaurants/(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view()),
    
]



