from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.core.mail import send_mail

User = settings.AUTH_USER_MODEL

class Trainee(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    # Trainee object is also related to dish_log, exercise_log, sleep_log, and weight_log

    activated       = models.BooleanField(default=False)
    join_date       = models.DateTimeField(auto_now_add=True)
 