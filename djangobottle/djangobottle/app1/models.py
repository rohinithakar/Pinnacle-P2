from django.db import models

# Create your models here.
class MoocInstance(models.Model):
    team_name = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    default = models.BooleanField()
    def __unicode__(self):
        return 'Mooc Name: ' + self.team_name
