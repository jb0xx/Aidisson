from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.core.mail import send_mail

User = settings.AUTH_USER_MODEL

class Trainee(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    
    activated       = models.BooleanField(default=False)
    join_date       = models.DateTimeField(auto_now_add=True)
    original_weight = models.DecimalField(max_digits=6, decimal_places=3, default=0)


    def __str__(self):
    	return self.get_username()


    def get_user(self):
    	return self.user


    def get_username(self):
    	return self.user.username


    # def get_original_weight(self):
    #     return self.original_weight
 