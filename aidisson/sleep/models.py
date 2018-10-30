import math

from django.db import models

from users.models import Trainee

# Create your models here.
class Session(models.Model):
    trainee     = models.ForeignKey(Trainee, on_delete=models.CASCADE)
    starttime   = models.DateTimeField(null=True)
    endtime     = models.DateTimeField(null=True)
    quality     = models.FloatField()

    def __str__(self):
        user = self.trainee.user.username
        date = self.starttime.date()
        return f"{user}: {date}"
    

    def get_duration(self):
        """ returns duration of sleep session in minutes """
        dt = self.endtime - self.starttime
        hours = dt.seconds / 3600
        minutes = (dt.seconds / 60) % 60
        duration = {"hours": round(hours), "minutes": round(minutes)}
        return duration

    # def get_quality(self):
    # def set_quality(self):



class Cycle(models.Model):
    """ cycles are marked by a Light1 or Awake to initiate """
    # Constants
    AWAKE = 'Awake'
    LIGHT1 = 'NREM1'
    LIGHT2 = 'NREM2'
    DEEP = 'NREM3'
    REM = 'REM'
    SLEEP_STAGES = (
        (AWAKE, 'Awake'),
        (LIGHT1, 'Light1'),
        (LIGHT2, 'Light2'),
        (DEEP, 'Deep'),
        (REM, 'REM'),
    )

    # Variables
    session     = models.ForeignKey(Session, on_delete=models.CASCADE)
    starttime   = models.DateTimeField(null=True)
    endtime     = models.DateTimeField(null=True)
    stage       = models.CharField(
                        max_length=5,
                        choices=SLEEP_STAGES,
                        default=LIGHT1)


    def __str__(self):
        session = self.session
        time = self.starttime.time()
        return f"{session}  {time}"
