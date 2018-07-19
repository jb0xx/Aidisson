from django.db import models

from users.models import Trainee
# Create your models here.
class Log(models.Model):
    POUNDS      = 'lbs'
    KILOS       = 'kg'
    UNITS       = (
        (POUNDS, 'pounds'),
        (KILOS, 'kilograms')
        )

    trainee         = models.ForeignKey(Trainee, on_delete=models.CASCADE)
    log_datetime    = models.DateTimeField(auto_now_add=True)
    units           = models.CharField(max_length=3, choices=UNITS, default=POUNDS)
    weight          = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    

    def __str__(self):
        user = self.trainee.user.username
        date = self.log_datetime.date()
        return f"{user}: {date}"

