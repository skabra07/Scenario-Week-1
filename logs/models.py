from django.db import models
from datetime import datetime 

# Create your models here.
class Log(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.TextField(models.ForeignKey('User',on_delete=models.DO_NOTHING))
    createdTime = models.DateTimeField(default=datetime.now, blank=True)
    description = models.CharField(default="",max_length=5000)


    
