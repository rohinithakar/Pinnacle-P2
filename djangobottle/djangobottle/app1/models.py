from django.db import models

# Create your models here.
class MoocInstance(models.Model):
    team_name = models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    default = models.BooleanField()
