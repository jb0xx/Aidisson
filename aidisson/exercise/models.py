from django.db import models

from users.models import Trainee

# Create your models here.
class Workout(models.Model):
    trainee     = models.ForeignKey(Trainee, on_delete=models.CASCADE)
    starttime   = models.DateTimeField(null=True)
    endtime     = models.DateTimeField(null=True) 
    intensity   = models.DecimalField(max_digits=5, decimal_places=3, default=0)


    def __str__(self):
        user = self.trainee.user.username
        date = self.starttime.date()
        return f"{user}: {date}"


